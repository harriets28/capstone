// ---- Nav scroll behaviour ----
const nav = document.querySelector(".site-nav");
if (nav) {
    function updateNav() {
        nav.classList.toggle("scrolled", window.scrollY > 50);
        nav.style.boxShadow =
            window.scrollY > 10 ? "0 2px 16px rgba(26,22,18,.08)" : "none";
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
