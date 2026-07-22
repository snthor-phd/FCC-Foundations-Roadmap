# Foundations — Faircreek Church

An interactive **Adult Spiritual Formation** teaching roadmap for **Foundations**, a guided path through Scripture and the essentials of following Jesus. The site presents six classes of three weeks each — 54 short teaching sessions in all — organized as a browsable journey, styled to match [Faircreek Church](https://faircreek.org)'s brand (logo, colors, and typography).

**Live site:** _enable GitHub Pages (see below) and your URL will be_ `https://<username>.github.io/<repo>/`

## The roadmap

| Class | Title | Weeks |
|------|-------|-------|
| 1 | Understanding the Story of the Bible | The Story of the Bible · The Old Testament · The New Testament |
| 2 | How to Read the Bible Well | Bible Overview · Interpretation · Application |
| 3 | How to Follow Jesus | The Invitation · The Way of Jesus · Clash of Kingdoms |
| 4 | Understanding Who God Is | The Father · The Son · The Holy Spirit |
| 5 | Understanding Your New Identity | The Way God Sees Us · Our New Reality · Our New Family |
| 6 | How to Establish Spiritual Habits | Rebranding Spiritual Disciplines · Getting Started · Stretching Our Faith Muscles |

Each week is built the same way: three short teaching videos ("sessions"), each followed by table discussion, landing on one clear **bottom line**. Class time runs about 90 minutes.

## What's here

- `index.html` — the roadmap site (single page, no build step)
- `data.js` — all content (units, weeks, sessions, scripture, discussion questions), editable in plain JavaScript
- `.nojekyll` — tells GitHub Pages to serve files as-is

## Publish with GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Select branch `main` and folder `/ (root)`, then **Save**.
5. Wait ~1 minute; your site appears at `https://<username>.github.io/<repo>/`.

## Editing content

All teaching content lives in `data.js` as a plain object. To adjust a week, edit its `sessions`, `verses`, `questions`, or `bottomLine` — no rebuild needed, just refresh.

## Source

Content is summarized from the series **facilitator guides**. Those guides remain the authoritative source for full run sheets, timing, and slide notes.
