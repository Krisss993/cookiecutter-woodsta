import '../sass/project.scss';

/* Project specific Javascript goes here. */
document.addEventListener("DOMContentLoaded", function () {
  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth"
      });
    });
  });

  // Add slight fade-in effect on scroll
  const elements = document.querySelectorAll('.hero-section, .services-section, .cta-section');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
      }
    });
  });

  elements.forEach(el => observer.observe(el));
});
