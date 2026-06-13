document.addEventListener("DOMContentLoaded", function () {
  const players = Array.from(document.querySelectorAll(".js-player"));

  players.forEach((player) => {
    new Plyr(player, {
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
        options: [0.75, 1, 1.25, 1.5],
      },
    });
  });
});