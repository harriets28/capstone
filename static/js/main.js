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

// ---- Like button AJAX toggle ----
const likeBtn = document.getElementById("like-btn");
if (likeBtn) {
    likeBtn.addEventListener("click", async () => {
        const url = likeBtn.dataset.url;
        const csrf = document.cookie.match(/csrftoken=([^;]+)/)?.[1] || "";

        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrf,
                    "Content-Type": "application/json",
                },
            });
            const data = await response.json();
            const countEl = document.getElementById("like-count");

            if (data.liked) {
                likeBtn.classList.remove("btn-outline-danger");
                likeBtn.classList.add("btn-danger");
            } else {
                likeBtn.classList.remove("btn-danger");
                likeBtn.classList.add("btn-outline-danger");
            }
            countEl.textContent = data.like_count;
        } catch (err) {
            console.error("Like toggle failed:", err);
        }
    });
}
