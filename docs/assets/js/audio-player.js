document.addEventListener("DOMContentLoaded", function () {
  const players = Array.from(document.querySelectorAll(".js-player"));

  players.forEach((audio) => {
    new Plyr(audio, {
      captions: {
        active: true,
        update: true,
        language: "en",
      },
      controls: [
        "play",
        "progress",
        "current-time",
        "duration",
        "mute",
        "volume",
        "captions",
        "settings",
        "download",
      ],
      settings: ["captions", "speed"],
      speed: {
        selected: 1,
        options: [0.75, 1, 1.25, 1.5, 2],
      },
    });
  });

  setupAudioCaptionBox("lesson-01-audio", "lesson-01-caption-box");
});

function setupAudioCaptionBox(audioId, captionBoxId) {
  const audio = document.getElementById(audioId);
  const captionBox = document.getElementById(captionBoxId);

  if (!audio || !captionBox) {
    return;
  }

  const tracks = audio.textTracks;

  if (!tracks || tracks.length === 0) {
    captionBox.textContent = "No caption track found.";
    return;
  }

  const track = tracks[0];

  // Keep the browser from trying to render captions itself,
  // but still allow JavaScript to read the active cue.
  track.mode = "hidden";

  track.addEventListener("cuechange", function () {
    const activeCues = track.activeCues;

    if (!activeCues || activeCues.length === 0) {
      captionBox.textContent = "";
      return;
    }

    captionBox.textContent = activeCues[0].text;
  });
}