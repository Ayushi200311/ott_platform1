document.addEventListener("DOMContentLoaded", function () {
  const video = document.getElementById("video");
  const playPauseBtn = document.getElementById("playPauseBtn");
  const controls = document.getElementById("videoControls");

  // ✅ Autoplay if coming from another page (e.g. home)
  if (document.referrer && document.referrer.includes(window.location.origin + "/")) {
    video.play().catch(err => console.warn("Autoplay blocked:", err));
  }

  // ✅ Toggle play/pause icon
  video.addEventListener("play", () => {
    playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
  });

  video.addEventListener("pause", () => {
    playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
  });

  // ✅ Show controls when mouse moves in fullscreen
  document.addEventListener("fullscreenchange", () => {
    if (document.fullscreenElement === video || document.fullscreenElement?.contains(video)) {
      controls.style.opacity = 1;

      video.addEventListener("mousemove", () => {
        controls.style.opacity = 1;
        clearTimeout(window._hideControlsTimeout);
        window._hideControlsTimeout = setTimeout(() => {
          controls.style.opacity = 0;
        }, 2000);
      });
    }
  });
});

// Controls: Play/pause and seek
function togglePlayPause() {
  const video = document.getElementById("video");
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
}

function seekVideo(seconds) {
  const video = document.getElementById("video");
  video.currentTime += seconds;
}


function toggleFullscreen() {
  const wrapper = document.getElementById("videoWrapper");

  if (!document.fullscreenElement) {
    if (wrapper.requestFullscreen) {
      wrapper.requestFullscreen();
    } else if (wrapper.webkitRequestFullscreen) { /* Safari */
      wrapper.webkitRequestFullscreen();
    } else if (wrapper.msRequestFullscreen) { /* IE11 */
      wrapper.msRequestFullscreen();
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    }
  }
}
