// ---- Nav scroll behaviour ----
const nav = document.querySelector(".site-nav");
if (nav) {
    function updateNav() {
        const isScrolled = window.scrollY > 50;
        nav.classList.toggle("scrolled", isScrolled);
        nav.style.boxShadow =
            window.scrollY > 10 ? "0 2px 16px rgba(26,22,18,.08)" : "none";

        const hasHero = document.querySelector(".parallax-hero");
        if (hasHero) {
            nav.classList.toggle("on-hero", !isScrolled);
        }
    }
    window.addEventListener("scroll", updateNav, { passive: true });
    updateNav();
}

// ---- Auto-dismiss flash messages after 5 seconds ----
document.querySelectorAll(".alert-toast").forEach((toast) => {
    setTimeout(() => {
        toast.style.transition = "opacity .4s ease";
        toast.style.opacity = "0";
        setTimeout(() => toast.remove(), 400);
    }, 5000);
});

// ---- Mobile menu ----
const mobileMenuBtn = document.getElementById("mobile-menu-btn");
const navLinks = document.querySelector(".nav-links");
if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener("click", () => {
        const isOpen = navLinks.classList.toggle("open");
        mobileMenuBtn.textContent = isOpen ? "Close" : "Menu";
    });
}
