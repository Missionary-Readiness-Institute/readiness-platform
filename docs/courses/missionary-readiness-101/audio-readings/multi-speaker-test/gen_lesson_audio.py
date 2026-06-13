import json
import subprocess
from pathlib import Path
from html import escape

from google.cloud import texttospeech

SEGMENTS_FILE = "lesson-01-dialogue.json"
OUT_DIR = Path("lesson-01-audio")

FINAL_WAV = "lesson-01-dialogue.wav"
FINAL_MP3 = "lesson-01-dialogue.mp3"
FINAL_VTT = "lesson-01-dialogue.vtt"

LANGUAGE_CODE = "en-US"

SILENCE_FILE = OUT_DIR / "silence.wav"
SILENCE_SECONDS = 0.35
SAMPLE_RATE = "24000"

OUT_DIR.mkdir(exist_ok=True)

client = texttospeech.TextToSpeechClient()


def run_command(args):
    subprocess.run(args, check=True)


def get_audio_duration_seconds(audio_file: Path) -> float:
    """
    Uses ffprobe to get the duration of an audio file in seconds.
    Requires ffmpeg/ffprobe to be installed.
    """
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(audio_file),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    return float(result.stdout.strip())


def format_vtt_timestamp(seconds: float) -> str:
    """
    Formats seconds as WebVTT timestamp: HH:MM:SS.mmm
    """
    if seconds < 0:
        seconds = 0

    hours = int(seconds // 3600)
    seconds %= 3600

    minutes = int(seconds // 60)
    seconds %= 60

    whole_seconds = int(seconds)
    milliseconds = int(round((seconds - whole_seconds) * 1000))

    # Handle rounding overflow, e.g. 59.9996 -> 60.000
    if milliseconds == 1000:
        milliseconds = 0
        whole_seconds += 1

    if whole_seconds == 60:
        whole_seconds = 0
        minutes += 1

    if minutes == 60:
        minutes = 0
        hours += 1

    return f"{hours:02d}:{minutes:02d}:{whole_seconds:02d}.{milliseconds:03d}"


def wrap_caption_text(text: str, speaker: str | None = None) -> str:
    """
    Creates the text shown in the caption.
    WebVTT supports plain text. Avoid HTML unless you specifically want markup.
    """
    text = " ".join(text.strip().split())

    if speaker:
        speaker_label = speaker.capitalize()
        return f"{speaker_label}: {text}"

    return text


# Create silence file if missing
if not SILENCE_FILE.exists() or SILENCE_FILE.stat().st_size == 0:
    run_command(
        [
            "ffmpeg",
            "-y",
            "-f", "lavfi",
            "-i", f"anullsrc=r={SAMPLE_RATE}:cl=mono",
            "-t", str(SILENCE_SECONDS),
            "-acodec", "pcm_s16le",
            str(SILENCE_FILE),
        ]
    )
    print(f"Created {SILENCE_FILE}")
else:
    print(f"Using existing {SILENCE_FILE}")


with open(SEGMENTS_FILE, "r", encoding="utf-8") as f:
    segments = json.load(f)


wav_files = []
caption_entries = []

for index, segment in enumerate(segments, start=1):
    speaker = segment["speaker"]
    voice_name = segment["voice"]
    text = segment["text"].strip()

    if not text:
        continue

    output_file = OUT_DIR / f"{index:03d}-{speaker}.wav"

    # Reuse existing WAV if available
    if output_file.exists() and output_file.stat().st_size > 0:
        print(f"Using existing {output_file}")
    else:
        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code=LANGUAGE_CODE,
            name=voice_name,
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        )

        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config,
        )

        with open(output_file, "wb") as out:
            out.write(response.audio_content)

        print(f"Created {output_file}")

    wav_files.append(
        {
            "file": output_file,
            "speaker": speaker,
            "text": text,
        }
    )


# Build concat list and VTT timing map
concat_file = OUT_DIR / "concat.txt"

current_time = 0.0

with open(concat_file, "w", encoding="utf-8") as concat:
    for i, item in enumerate(wav_files):
        wav = item["file"]
        speaker = item["speaker"]
        text = item["text"]

        duration = get_audio_duration_seconds(wav)

        start_time = current_time
        end_time = current_time + duration

        caption_entries.append(
            {
                "start": start_time,
                "end": end_time,
                "speaker": speaker,
                "text": text,
            }
        )

        concat.write(f"file '{wav.resolve()}'\n")

        current_time = end_time

        # Add silence after every segment except the last one
        if i < len(wav_files) - 1:
            concat.write(f"file '{SILENCE_FILE.resolve()}'\n")
            current_time += SILENCE_SECONDS


# Write VTT file
with open(FINAL_VTT, "w", encoding="utf-8") as vtt:
    vtt.write("WEBVTT\n\n")

    for index, entry in enumerate(caption_entries, start=1):
        start = format_vtt_timestamp(entry["start"])
        end = format_vtt_timestamp(entry["end"])
        caption_text = wrap_caption_text(entry["text"], entry["speaker"])

        vtt.write(f"{index}\n")
        vtt.write(f"{start} --> {end}\n")
        vtt.write(f"{caption_text}\n\n")

print(f"Created VTT: {FINAL_VTT}")


# Combine WAV files
run_command(
    [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        FINAL_WAV,
    ]
)

# Normalize and convert to MP3
run_command(
    [
        "ffmpeg",
        "-y",
        "-i", FINAL_WAV,
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-codec:a", "libmp3lame",
        "-b:a", "192k",
        FINAL_MP3,
    ]
)

print(f"Final WAV: {FINAL_WAV}")
print(f"Final MP3: {FINAL_MP3}")
print(f"Final VTT: {FINAL_VTT}")