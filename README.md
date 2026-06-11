# Mohammad Saud — Personal Portfolio

A handcrafted, single-page portfolio website. Pure HTML + CSS + vanilla JavaScript —
no build step, no dependencies, nothing to install. Open `index.html` in a browser and it works.

## Structure

```
portfolio/
├── index.html              ← all content lives here (edit this to update text)
├── css/style.css           ← design system (colours, layout, dark mode, responsive)
├── js/main.js              ← scroll animations, nav, theme toggle, contact form
├── assets/
│   ├── profile.jpg         ← ADD THIS: your photo (portrait, ~800×1000px)
│   ├── profile-placeholder.svg
│   ├── Mohammad-Saud-Resume.pdf
│   └── gallery/            ← ADD THESE: your real work images (see below)
└── tools/make_resume.py    ← regenerates the resume PDF (optional)
```

## ✅ Before you publish

1. **Photo** — done: your LinkedIn profile photo is already in place as
   `assets/profile.jpg`. Replace that file anytime to update it.

2. **Add gallery images** — drop real screenshots/photos into `assets/gallery/`
   using these exact filenames (placeholders are replaced automatically):

   | Filename | What to put there |
   |---|---|
   | `kidneymate-ui.png` | KidneyMate app screenshots |
   | `vas-map.png` | VAS portal / soil map screenshot |
   | `retailsense-dashboard.png` | RetailSenseAI dashboard |
   | `forge-pitch.jpg` | Photo of you pitching at FORGE |
   | `cerdi-work.jpg` | GIS / archive work at CeRDI |
   | `certificates.jpg` | Certificates / milestones |

3. **Dates & details** — taken from your LinkedIn profile (June 2026):
   BRAC University Oct 2021 – Jun 2023 · FedUni Jun 2023 – Jun 2026 ·
   CeRDI co-op placement Oct 2025 – Present · KidneyMate founded Jan 2026.
   If anything changes, edit `index.html` and `tools/make_resume.py`, then re-run
   `python tools/make_resume.py` (or just replace `assets/Mohammad-Saud-Resume.pdf`
   with your own exported PDF).

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

## 🚀 Deploy free on GitHub Pages (step by step)

The git repository is already initialised with your first commit. Now:

**Step 1 — Create the GitHub repository**
1. Go to [github.com/new](https://github.com/new) (logged in as `msaud1959`)
2. Repository name: `msaud1959.github.io` ← this exact name gives you the cleanest URL
   (or any name like `portfolio` — URL becomes `msaud1959.github.io/portfolio`)
3. Keep it **Public**, do **not** tick "Add a README"
4. Click **Create repository**

**Step 2 — Push this folder**
Open a terminal in this `portfolio` folder and run:

```
git remote add origin https://github.com/msaud1959/msaud1959.github.io.git
git branch -M main
git push -u origin main
```

(Git will ask you to log in to GitHub in a browser window the first time.)

**Step 3 — Turn on GitHub Pages**
1. On the repo page: **Settings → Pages** (left sidebar)
2. Under "Build and deployment" → Source: **Deploy from a branch**
3. Branch: **main**, folder: **/ (root)** → **Save**

**Step 4 — Open your live site**
After ~1–2 minutes your site is live at:

> **https://msaud1959.github.io/**

(or `https://msaud1959.github.io/portfolio/` if you used a custom repo name)

**Updating the live site later** — edit files, then:

```
git add -A
git commit -m "Update content"
git push
```

The site refreshes automatically within a minute or two.

### Alternative free hosts (same folder works as-is)

- **Netlify** — [app.netlify.com/drop](https://app.netlify.com/drop): drag the folder onto the page, done
- **Vercel** — `vercel.com/new`, import the GitHub repo, framework preset "Other"

---

Designed & built by hand. © Mohammad Saud
