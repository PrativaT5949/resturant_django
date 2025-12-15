"use strict";

// Dropdown on mouse hover for screen width >= 992px
const dropdowns = document.querySelectorAll(".dropdown");
const dropdownToggles = document.querySelectorAll(".dropdown-toggle");
const dropdownMenus = document.querySelectorAll(".dropdown-menu");
const showClass = "show";

function handleDropdownHover() {
  if (window.matchMedia("(min-width: 992px)").matches) {
    dropdowns.forEach((dropdown) => {
      dropdown.addEventListener("mouseenter", () => {
        dropdown.classList.add(showClass);
        const toggle = dropdown.querySelector(".dropdown-toggle");
        const menu = dropdown.querySelector(".dropdown-menu");
        if (toggle) toggle.setAttribute("aria-expanded", "true");
        if (menu) menu.classList.add(showClass);
      });
      dropdown.addEventListener("mouseleave", () => {
        dropdown.classList.remove(showClass);
        const toggle = dropdown.querySelector(".dropdown-toggle");
        const menu = dropdown.querySelector(".dropdown-menu");
        if (toggle) toggle.setAttribute("aria-expanded", "false");
        if (menu) menu.classList.remove(showClass);
      });
    });
  } else {
    dropdowns.forEach((dropdown) => {
      dropdown.removeEventListener("mouseenter", null);
      dropdown.removeEventListener("mouseleave", null);
    });
  }
}

window.addEventListener("load", handleDropdownHover);
window.addEventListener("resize", handleDropdownHover);

// Back to top button
const backToTopBtn = document.querySelector(".back-to-top");
window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    backToTopBtn.style.display = "block";
    backToTopBtn.style.opacity = 1;
  } else {
    backToTopBtn.style.opacity = 0;
    backToTopBtn.style.display = "none";
  }
});
backToTopBtn.addEventListener("click", function (e) {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: "smooth" });
});

// Modal Video
document.addEventListener("DOMContentLoaded", function () {
  let videoSrc;

  document.querySelectorAll(".btn-play").forEach((btn) => {
    btn.addEventListener("click", function () {
      videoSrc = this.getAttribute("data-src");
      console.log(videoSrc);
    });
  });

  const videoModal = document.getElementById("videoModal");
  const video = document.getElementById("video");

  if (videoModal) {
    videoModal.addEventListener("shown.bs.modal", function () {
      if (video && videoSrc) {
        video.setAttribute(
          "src",
          `${videoSrc}?autoplay=1&amp;modestbranding=1&amp;showinfo=0`
        );
      }
    });

    videoModal.addEventListener("hide.bs.modal", function () {
      if (video && videoSrc) {
        video.setAttribute("src", videoSrc);
      }
    });
  }
});

// Spinner hide on load
window.addEventListener("load", function () {
  const spinner = document.getElementById("spinner");
  if (spinner) {
    spinner.style.display = "none";
    console.log("Spinner hidden");
  } else {
    console.log("Spinner element not found");
  }
});

// Sticky navbar
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// Menu tab behaviors and smooth scroll for back-to-top button
document.addEventListener("DOMContentLoaded", function () {
  if (backToTopBtn) {
    backToTopBtn.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  document.querySelectorAll('a[data-bs-toggle="pill"]').forEach((tab) => {
    tab.addEventListener("shown.bs.tab", function (e) {
      console.log("Active tab:", e.target.textContent.trim());
    });
  });
});

// Optional spinner fade out effect
window.addEventListener("load", function () {
  const spinner = document.getElementById("spinner");
  if (spinner) {
    spinner.classList.add("hide");
    setTimeout(() => {
      spinner.style.display = "none";
    }, 300);
  }
});
//To Change the color while scroll in nav bar
window.addEventListener("scroll", function () {
  var navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    // Change 50 to the scroll distance you prefer
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});
const videoModal = document.getElementById("videoModal");
const videoSrcInput = videoModal.querySelector("#video");

videoModal.addEventListener("show.bs.modal", (event) => {
  const button = event.relatedTarget;
  const videoSrc = button.getAttribute("data-src");
  videoSrcInput.src = videoSrc + "?autoplay=1&modestbranding=1&showinfo=0";
});

videoModal.addEventListener("hidden.bs.modal", () => {
  videoSrcInput.src = "";
});
// for booking page video modal
var modal = document.getElementById("videoModal");
var video = document.getElementById("video");

modal.addEventListener("show.bs.modal", function () {
  video.muted = true; // mute the video to allow autoplay
  video.play(); // start playing video when modal opens
});

modal.addEventListener("hidden.bs.modal", function () {
  video.pause(); // pause/reset video on modal close
  video.currentTime = 0; // reset to start
});
