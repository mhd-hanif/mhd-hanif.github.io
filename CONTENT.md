# Updating the site

Everything on the site is a Markdown file or a YAML data file. There is no CMS
and no database — edit a file, commit, and GitHub Pages rebuilds within a minute
or two.

## Where things live

| What | Where |
|---|---|
| Publications | `_publications/*.md` — one file per paper |
| Projects | `_portfolio/*.md` — one file per project |
| Talks | `_talks/*.md` |
| Teaching | `_teaching/*.md` |
| News items | `_data/news.yml` |
| Affiliations strip | `_data/affiliations.yml` |
| Skills chips | `_data/stack.yml` |
| Awards / service (CV page only) | `_data/awards.yml`, `_data/service.yml` |
| Bio, contact text | `_pages/about.md` |
| Name, tagline, social links, CV link | `_config.yml` |
| Images | `images/` |

---

## Adding or updating a teaser image or GIF

This is the one part with a build step, because the source files are large: the
GIFs in `images/` run 3–11 MB each, and the homepage shows several at once.
Rather than serving those directly, each teaser gets two small derived files.

**1. Put the source file in `images/.`** Any name works; `portf_<something>.gif`
matches the existing convention. Keep the original — it is what the detail page
shows at full size.

**2. Point the entry at it** in the front matter:

```yaml
teaser: "/images/portf_mynewthing.gif"
```

**3. Run the build script:**

```bash
pip install Pillow          # once
python3 tools/build-teasers.py
```

It creates `images/thumbs/portf_mynewthing.jpg` (a still, ~40 KB) and, for GIFs,
`images/motion/portf_mynewthing.webp` (a ~6 second loop, ~200 KB), then writes
`thumb:` and `motion:` into the front matter for you.

**4. Commit all of it** — the source, both derived files, and the `.md`.

Notes:

- Re-running is safe. Existing files are skipped, and an existing `thumb:` or
  `motion:` value is never overwritten — a few entries point at a hand-picked
  frame so two cards using the same GIF don't look identical. Use `--force` to
  genuinely rebuild.
- `--check` reports what would be built without changing anything.
- Static images (PNG/JPG) get a thumbnail but no animation, which is correct.
- If you'd rather not run the script, just commit the source GIF with `teaser:`
  set and ask — the derived files can be generated for you.

### Starting from a video instead of a GIF

If the source is a video — a YouTube recording, a screen capture, a simulation
export — don't make a GIF first. GIF is a poor intermediate: the same six
seconds is 3–11 MB as GIF and around 200 KB as WebP, with better colour.
`tools/clip-to-teaser.py` goes straight from the video to all three files:

```bash
pip install imageio-ffmpeg            # once, if ffmpeg isn't installed
python3 tools/clip-to-teaser.py demo.mp4 --name portf_myproject \
    --start 00:01:30 --duration 6

# or straight from YouTube (pip install yt-dlp first)
python3 tools/clip-to-teaser.py --url "https://youtu.be/XXXX" \
    --name portf_myproject --start 00:01:30 --duration 6
```

It writes `images/portf_myproject.webp` (detail page), plus the card thumbnail
and animation, and prints the three front-matter lines to paste in. Useful
extras:

- `--crop W:H:X:Y` — trim letterboxing, or focus on one pane of a multi-pane
  recording, applied before scaling
- `--fps` — default 10, which suits a screen capture and keeps files small
- `--thumb-at` — which second of the clip to freeze for the still
- `--gif` — also write a GIF, if you want one for slides or social media

Pick a segment that reads at thumbnail size: clear movement, not too much fine
text.

### Why not just use the GIF directly?

A GIF in the card would work, but 40 MB of teasers on one page would not. The
derived files bring that to ~1.6 MB. The animation is served through a
`<picture>` element gated on `prefers-reduced-motion`, so visitors who have
asked their system to reduce motion get the still instead.

---

## Adding a publication

Create `_publications/<year>-<type>-<name>.md`:

```yaml
---
title: "Paper Title Here"
collection: publications
category: conferences        # manuscripts | books | conferences | domestic | thesis | patents
permalink: /publication/2026-paper-yourname
date: 2026-06-01
sortdate: 2026-06-01         # controls ordering; can differ from date
venue: "Conference Name, 2026"
venueshort: "ICRA"           # shown if there is no teaser image
authors: '<span class="me">Muhammad Hanif</span>, Second Author, Third Author'
note: "pp. 100–110."         # optional
status: "Under review"       # optional badge
teaser: "/images/portf_x.gif"
paperurl: "https://..."
video: "https://..."
code: "https://..."
project: "/portfolio/some-project/"   # see "Where a publication title links to"
featured: true               # show on the homepage
bibtex: |
  @inproceedings{key2026,
    title  = {...},
    author = {...},
    year   = {2026}
  }
---

Optional body text, shown on the publication's own page.
```

Wrap your own name in `<span class="me">…</span>` so it is highlighted in the
author list.

## Adding a project

Create `_portfolio/<slug>.md`:

```yaml
---
title: "Project Title"
collection: portfolio
permalink: /portfolio/your-slug/
order: 5                     # position in the grid, low numbers first
summary: "One or two sentences shown on the card."
teaser: "/images/portf_x.gif"
period: "2025 – 2026"
collaborator: "Company Name" # optional
tags: ["ROS2", "Unity", "Control"]     # first 3 show on the card
featured: true               # show on the homepage
publications:                # renders "Publications from this project"
  - "/publication/2026-paper-yourname"
---

Body text in Markdown. Images, videos and headings all work.
```

The `publications:` list takes the `permalink` values from the publication
files. Setting `project:` on those publications gives you the link back.

## Where a publication title links to

A publication card has one destination, and its title, its teaser image and its
"Project Page" chip all share it. `project:` decides which:

| `project:` in the front matter | Title and chip lead to |
| --- | --- |
| an external URL — `https://htnk-lab.github.io/coverage-recon/` | that page, in a new tab |
| an internal permalink — `/portfolio/angle-aware-coverage/` | the project page on this site |
| not set | the publication's own page; no chip is shown |

Prefer an external project page when the group has published one — those carry
the full video set. Point at a `_portfolio/` entry otherwise, and leave
`project:` out only when the paper belongs to no project on the site.

One exception keeps the site navigable: on a project page, the cards for that
project's own publications ignore `project:` and link to each paper's own page,
so nothing becomes unreachable by linking outward.

## Adding a news item

Newest first, in `_data/news.yml`:

```yaml
- date: "Jun 2026"
  text: >-
    Our paper <em>Title</em> was accepted at <strong>Venue</strong>.
```

Inline HTML is allowed. The homepage shows the first six behind a "show all"
toggle; change `news_visible` in `_pages/about.md` to adjust.

## Adding a talk

Create `_talks/<date>-<slug>.md`:

```yaml
---
title: "The title of the talk itself"
collection: talks
type: "Invited Talk"         # or International Conference, Plenary Talk, …
event: "Conference or workshop name"
permalink: /talks/2026-06-01-slug
venue: "Host institution"    # omit if it duplicates `event`
date: 2026-06-01
location: "City, Country"
---
```

The heading is the **talk title**, not the event — the event goes in `event:`.

---

## Checking your work before pushing

```bash
bundle install               # once
bundle exec jekyll serve     # http://localhost:4000
```

If Jekyll isn't installed locally, pushing to a branch and opening a pull
request also works — just be aware the live site only rebuilds from `master`.
