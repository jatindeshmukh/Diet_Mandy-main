// ✅ Highlight nav link on scroll
const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll("nav ul li a");

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY + 100;
        let offset = sec.offsetTop;
        let height = sec.offsetHeight;
        let id = sec.getAttribute("id");

        if (top >= offset && top < offset + height) {
            navLinks.forEach(link => link.classList.remove("active"));
            document.querySelector(`nav ul li a[href*=${id}]`).classList.add("active");
        }
    });
};