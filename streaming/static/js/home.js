// document.addEventListener("DOMContentLoaded", () => {
//   let currentIndex = 0;
//   const slides = document.getElementById("slides");
//   const slideItems = slides.querySelectorAll(".slide");
//   const totalSlides = slideItems.length;
//   const dotsContainer = document.getElementById("dots");

//   // Generate dots
//   for (let i = 0; i < totalSlides; i++) {
//     const dot = document.createElement("div");
//     dot.classList.add("dot");
//     dot.addEventListener("click", () => goToSlide(i));
//     dotsContainer.appendChild(dot);
//   }

//   const dots = document.querySelectorAll(".dot");

//   function updateSlide() {
//     slides.style.transform = `translateX(-${currentIndex * 100}vw)`;
//     dots.forEach((dot, i) => {
//       dot.classList.toggle("active", i === currentIndex);
//     });
//   }

//   function nextSlide() {
//     currentIndex = (currentIndex + 1) % totalSlides;
//     updateSlide();
//   }

//   function prevSlide() {
//     currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
//     updateSlide();
//   }

//   function goToSlide(index) {
//     currentIndex = index;
//     updateSlide();
//   }

//   setInterval(nextSlide, 4000);
//   updateSlide();
// });






// function scrollMedia(type, direction) {
//   const carousel = document.getElementById(`carousel-${type}`);
//   const scrollAmount = 200;
//   carousel.scrollBy({ left: direction * scrollAmount, behavior: "smooth" });
// }







// home.js - Hero Carousel and Media Section functionality

// Hero Carousel
let currentSlide = 0;
const slides = document.querySelectorAll('.hero-slide');
const dots = document.querySelectorAll('.dot');
const totalSlides = slides.length;

function showSlide(index) {
    // Hide all slides
    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));
    
    // Show current slide
    slides[index].classList.add('active');
    dots[index].classList.add('active');
}

function changeSlide(direction) {
    currentSlide += direction;
    
    if (currentSlide >= totalSlides) {
        currentSlide = 0;
    } else if (currentSlide < 0) {
        currentSlide = totalSlides - 1;
    }
    
    showSlide(currentSlide);
}

function goToSlide(index) {
    currentSlide = index;
    showSlide(currentSlide);
}

// Auto-advance carousel
function startAutoSlide() {
    setInterval(() => {
        changeSlide(1);
    }, 5000);
}

// Media Section Scrolling
function scrollMediaSection(sectionId, direction) {
    const carousel = document.getElementById(`${sectionId}-carousel`);
    const scrollAmount = 240; // Width of card + gap
    
    carousel.scrollBy({
        left: direction * scrollAmount,
        behavior: 'smooth'
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Start auto-slide
    startAutoSlide();
    
    // Initialize first slide
    showSlide(0);
    
    console.log('Carousel initialized with', totalSlides, 'slides');
});

