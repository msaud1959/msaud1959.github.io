# Mohammad Saud — Personal Portfolio

A handcrafted, single-page portfolio website. Pure HTML + CSS + vanilla JavaScript —
no build step, no dependencies, nothing to install. Open `index.html` in a browser and it works.

## Structure

```
portfolio/
├── index.html              ← all content lives here (edit this to update text)
├── css/style.css           ← design system (colours, glass cards, glow, responsive)
├── js/main.js              ← animations, typed roles, cursor glow, theme, contact form
└── assets/
    ├── profile.jpg         ← your photo (from LinkedIn — replace anytime)
    ├── profile-placeholder.svg
    └── Mohammad-Saud-Resume.pdf   ← your uploaded resume (replace to update)
```

## ✅ Quick facts

- **Photo** — your LinkedIn profile photo, already in place as `assets/profile.jpg`.
- **Resume** — the download button serves `assets/Mohammad-Saud-Resume.pdf`
  (your own uploaded resume). To update it later, just overwrite that file
  with a new PDF of the same name.
- **Dates & details** — taken from your LinkedIn profile (June 2026):
  BRAC University Oct 2021 – Jun 2023 · FedUni Jun 2023 – Jun 2026 ·
  CeRDI co-op placement Oct 2025 – Present · KidneyMate founded Jan 2026.

### Optional: make the contact form deliver to your inbox

The form currently falls back to opening the visitor's email app (always works,
nothing to configure). For true in-page sending:

1. Create a free account at [formspree.io](https://formspree.io) (50 messages/month free)
2. Create a form, copy your endpoint (looks like `https://formspree.io/f/abcd1234`)
3. In `index.html`, replace `YOUR_FORM_ID` in the form's `action` attribute

## How to update content later

Everything is plain HTML — open `index.html` in any editor:

- **New job / experience** → copy one `<li class="t-item">…</li>` block in the
  Journey section and edit it
- **New project** → copy one `<article class="project">…</article>` block
- **New skills** → add `<li>Skill name</li>` inside the relevant `pill-list`
- **Colours / fonts** → edit the variables at the top of `css/style.css`

## 🚀 Deployment — LIVE

The site is deployed on GitHub Pages:

> **https://msaud1959.github.io/**

Repository: [github.com/msaud1959/msaud1959.github.io](https://github.com/msaud1959/msaud1959.github.io)
(public repo, Pages serves the `main` branch root automatically)

**Updating the live site** — edit files in this folder, then:

```
git add -A
git commit -m "Update content"
git push
```

The live site refreshes automatically within a minute or two.

---

Designed & built by hand. © Mohammad Saud
