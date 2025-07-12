// // document.addEventListener("DOMContentLoaded", function () {
// //   const video = document.getElementById("video");
// //   const playPauseBtn = document.getElementById("playPauseBtn");
// //   const controls = document.getElementById("videoControls");

// //   // ✅ Autoplay if coming from another page (e.g. home)
// //   if (document.referrer && document.referrer.includes(window.location.origin + "/")) {
// //     video.play().catch(err => console.warn("Autoplay blocked:", err));
// //   }

// //   // ✅ Toggle play/pause icon
// //   video.addEventListener("play", () => {
// //     playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
// //   });

// //   video.addEventListener("pause", () => {
// //     playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
// //   });

// //   // ✅ Show controls when mouse moves in fullscreen
// //   document.addEventListener("fullscreenchange", () => {
// //     if (document.fullscreenElement === video || document.fullscreenElement?.contains(video)) {
// //       controls.style.opacity = 1;

// //       video.addEventListener("mousemove", () => {
// //         controls.style.opacity = 1;
// //         clearTimeout(window._hideControlsTimeout);
// //         window._hideControlsTimeout = setTimeout(() => {
// //           controls.style.opacity = 0;
// //         }, 2000);
// //       });
// //     }
// //   });
// // });

// // // Controls: Play/pause and seek
// // function togglePlayPause() {
// //   const video = document.getElementById("video");
// //   if (video.paused) {
// //     video.play();
// //   } else {
// //     video.pause();
// //   }
// // }

// // function seekVideo(seconds) {
// //   const video = document.getElementById("video");
// //   video.currentTime += seconds;
// // }


// // function toggleFullscreen() {
// //   const wrapper = document.getElementById("videoWrapper");

// //   if (!document.fullscreenElement) {
// //     if (wrapper.requestFullscreen) {
// //       wrapper.requestFullscreen();
// //     } else if (wrapper.webkitRequestFullscreen) { /* Safari */
// //       wrapper.webkitRequestFullscreen();
// //     } else if (wrapper.msRequestFullscreen) { /* IE11 */
// //       wrapper.msRequestFullscreen();
// //     }
// //   } else {
// //     if (document.exitFullscreen) {
// //       document.exitFullscreen();
// //     } else if (document.webkitExitFullscreen) {
// //       document.webkitExitFullscreen();
// //     } else if (document.msExitFullscreen) {
// //       document.msExitFullscreen();
// //     }
// //   }
// // }




// document.addEventListener("DOMContentLoaded", function () {
//   const slides = document.querySelectorAll(".slide");
//   if (!slides || slides.length === 0) return; // ✅ Exit safely if no slides

//   const prevBtn = document.getElementById("prev-slide");
//   const nextBtn = document.getElementById("next-slide");

//   let currentSlide = 0;
//   const totalSlides = slides.length;

//   function showSlide(index) {
//     slides.forEach(slide => slide.classList.remove("active"));
//     if (slides[index]) {
//       slides[index].classList.add("active");
//     }
//   }

//   function changeSlide(offset) {
//     currentSlide = (currentSlide + offset + totalSlides) % totalSlides;
//     showSlide(currentSlide);
//   }

//   if (prevBtn) prevBtn.addEventListener("click", () => changeSlide(-1));
//   if (nextBtn) nextBtn.addEventListener("click", () => changeSlide(1));

//   showSlide(currentSlide);
//   setInterval(() => changeSlide(1), 5000);
// });



const slides = document.querySelectorAll(".slide");
let currentSlide = 0;

function showSlide(n) {
  if (slides[currentSlide]) slides[currentSlide].classList.remove("active");
  if (slides[n]) {
    slides[n].classList.add("active");
    currentSlide = n;
  }
}

function changeSlide(step) {
  const totalSlides = slides.length;
  const nextSlide = (currentSlide + step + totalSlides) % totalSlides;
  showSlide(nextSlide);
}

function startAutoSlide() {
  setInterval(() => changeSlide(1), 3000);
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("prev-slide")?.addEventListener("click", () => changeSlide(-1));
  document.getElementById("next-slide")?.addEventListener("click", () => changeSlide(1));
  startAutoSlide();
});
