// Smooth Scroll for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        const targetId = this.getAttribute("href");
        if (targetId !== "#") {
            document.querySelector(targetId).scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});

// Navbar Background Change on Scroll
window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 60) {
        navbar.style.background = "#fff";
        navbar.style.boxShadow = "0 3px 10px rgba(0, 0, 0, 0.15)";
    } else {
        navbar.style.background = "white";
        navbar.style.boxShadow = "0 3px 8px rgba(0, 0, 0, 0.1)";
    }
});

// Fade-in Animation for Feature Cards when in View
const cards = document.querySelectorAll(".card");

const appearOptions = {
    threshold: 0.2
};

const appearOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("appear");
        observer.unobserve(entry.target);
    });
}, appearOptions);

cards.forEach(card => {
    appearOnScroll.observe(card);
});

// Small Button Animation
const ctaBtn = document.querySelector(".cta-btn");
if (ctaBtn) {
    ctaBtn.addEventListener("mouseenter", () => {
        ctaBtn.style.transform = "scale(1.05)";
    });
    ctaBtn.addEventListener("mouseleave", () => {
        ctaBtn.style.transform = "scale(1)";
    });
}