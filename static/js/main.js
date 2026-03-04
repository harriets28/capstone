// ---- Sticky nav shadow on scroll ----
const nav = document.querySelector(".site-nav");
if (nav) {
    window.addEventListener(
        "scroll",
        () => {
            if (window.scrollY > 10) {
                nav.style.boxShadow = "0 2px 16px rgba(26,22,18,.08)";
            } else {
                nav.style.boxShadow = "none";
            }
        },
        { passive: true },
    );
}

// ---- Auto-dismiss flash messages after 5 seconds ----
document.querySelectorAll(".alert-toast").forEach((toast) => {
    setTimeout(() => {
        toast.style.transition = "opacity .4s ease";
        toast.style.opacity = "0";
        setTimeout(() => toast.remove(), 400);
    }, 5000);
});
