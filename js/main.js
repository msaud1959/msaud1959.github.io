/* Mohammad Saud — portfolio interactions. Vanilla JS, no dependencies. */

(function () {
  "use strict";

  /* ---------- footer year ---------- */
  document.getElementById("year").textContent = new Date().getFullYear();

  /* ---------- theme toggle (persisted) ---------- */
  const themeToggle = document.getElementById("themeToggle");
  const stored = localStorage.getItem("ms-theme");
  if (stored === "dark" || (!stored && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
    document.documentElement.setAttribute("data-theme", "dark");
  }
  themeToggle.addEventListener("click", function () {
    const isDark = document.documentElement.getAttribute("data-theme") === "dark";
    document.documentElement.setAttribute("data-theme", isDark ? "light" : "dark");
    localStorage.setItem("ms-theme", isDark ? "light" : "dark");
  });

  /* ---------- header shadow + scroll progress ---------- */
  const header = document.getElementById("siteHeader");
  const progress = document.getElementById("progressBar");
  function onScroll() {
    header.classList.toggle("scrolled", window.scrollY > 10);
    const max = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + "%";
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  const navToggle = document.getElementById("navToggle");
  const navLinks = document.getElementById("navLinks");
  navToggle.addEventListener("click", function () {
    const open = navLinks.classList.toggle("open");
    navToggle.classList.toggle("open", open);
    navToggle.setAttribute("aria-expanded", String(open));
  });
  navLinks.addEventListener("click", function (e) {
    if (e.target.closest("a")) {
      navLinks.classList.remove("open");
      navToggle.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });

  /* ---------- reveal on scroll ---------- */
  const revealObserver = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );
  document.querySelectorAll(".reveal").forEach(function (el) {
    revealObserver.observe(el);
  });

  /* ---------- active nav link while scrolling ---------- */
  const sections = Array.prototype.slice.call(document.querySelectorAll("section[id]"));
  const linkFor = {};
  document.querySelectorAll('.nav-links a[href^="#"]').forEach(function (a) {
    linkFor[a.getAttribute("href").slice(1)] = a;
  });
  const sectionObserver = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        const link = linkFor[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          document.querySelectorAll(".nav-links a.active").forEach(function (x) {
            x.classList.remove("active");
          });
          link.classList.add("active");
        }
      });
    },
    { rootMargin: "-40% 0px -55% 0px" }
  );
  sections.forEach(function (s) { sectionObserver.observe(s); });

  /* ---------- contact form ----------
     Works two ways:
     1. If you set a real Formspree endpoint in index.html (replace YOUR_FORM_ID),
        the form submits via fetch and shows inline status.
     2. Until then, it gracefully falls back to opening the visitor's
        email app with the message pre-filled (mailto). Nothing is lost. */
  const form = document.getElementById("contactForm");
  const status = document.getElementById("formStatus");
  const EMAIL = "msaud1959@gmail.com";

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const name = document.getElementById("cf-name").value.trim();
    const email = document.getElementById("cf-email").value.trim();
    const message = document.getElementById("cf-msg").value.trim();

    const endpoint = form.getAttribute("action");
    if (endpoint.indexOf("YOUR_FORM_ID") !== -1) {
      // Formspree not configured yet — open the visitor's mail client instead.
      const subject = encodeURIComponent("Portfolio contact from " + name);
      const body = encodeURIComponent(message + "\n\n— " + name + " (" + email + ")");
      window.location.href = "mailto:" + EMAIL + "?subject=" + subject + "&body=" + body;
      status.textContent = "// opening your email app…";
      return;
    }

    status.textContent = "// sending…";
    fetch(endpoint, {
      method: "POST",
      headers: { Accept: "application/json" },
      body: new FormData(form)
    })
      .then(function (res) {
        if (res.ok) {
          form.reset();
          status.textContent = "// message sent — thanks, I'll reply soon.";
        } else {
          throw new Error("send failed");
        }
      })
      .catch(function () {
        status.textContent = "// couldn't send — please email " + EMAIL + " directly.";
      });
  });
})();
