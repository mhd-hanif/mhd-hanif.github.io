#!/usr/bin/env python3
"""
Generate card thumbnails and animations from teaser images.

Why this exists
---------------
Source teasers are large -- the GIFs in images/ run 3-11 MB each. Putting those
straight into the cards would make the homepage ~30 MB. So each teaser gets two
derived files:

  images/thumbs/<name>.jpg    a still frame, ~40 KB, used as the card image and
                              as the fallback for anyone browsing with
                              "reduce motion" turned on
  images/motion/<name>.webp   a ~6 second animated loop, ~200 KB, used as the
                              card image for everyone else (GIFs only)

This script scans _publications/ and _portfolio/ for a `teaser:` field, builds
whatever is missing, and writes `thumb:` and `motion:` back into the front
matter. It is safe to re-run: existing files are skipped unless --force.

Usage
-----
    pip install Pillow
    python3 tools/build-teasers.py            # build what's missing
    python3 tools/build-teasers.py --force    # rebuild everything
    python3 tools/build-teasers.py --check    # report only, change nothing
"""

import argparse
import os
import re
import sys

try:
    from PIL import Image, ImageSequence
except ImportError:
    sys.exit("Pillow is required:  pip install Pillow")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLLECTIONS = ("_publications", "_portfolio")
THUMB_DIR = os.path.join(ROOT, "images", "thumbs")
MOTION_DIR = os.path.join(ROOT, "images", "motion")

THUMB_WIDTH = 760      # card slot is ~210px, so this is ample even at 3x
MOTION_WIDTH = 400     # animation only needs to cover the card slot
MOTION_MS = 6000       # cap the loop at ~6 seconds
THUMB_QUALITY = 82
MOTION_QUALITY = 50


def front_matter(text):
    m = re.match(r"^---\n(.*?\n)---\n", text, re.S)
    return m.group(1) if m else ""


def field(text, name):
    m = re.search(rf'^{name}:\s*"([^"]+)"\s*$', front_matter(text), re.M)
    return m.group(1) if m else None


def set_field(text, name, value, after):
    """Add a front-matter field next to `after`, if it isn't already set.

    An existing value is never overwritten: some entries deliberately point at a
    hand-picked frame (e.g. a different moment of the same GIF so two cards
    don't look identical), and that choice must survive a re-run.
    """
    if re.search(rf'^{name}:', front_matter(text), re.M):
        return text
    anchor = re.search(rf'^{after}:.*$', text, re.M)
    if not anchor:
        return text
    return text[:anchor.end()] + f'\n{name}: "{value}"' + text[anchor.end():]


def build_thumb(src, dst):
    im = Image.open(src)
    im.seek(0)                                    # first frame for animations
    im = im.convert("RGB")
    w, h = im.size
    if w > THUMB_WIDTH:
        im = im.resize((THUMB_WIDTH, round(h * THUMB_WIDTH / w)), Image.LANCZOS)
    im.save(dst, "JPEG", quality=THUMB_QUALITY, optimize=True, progressive=True)


def build_motion(src, dst):
    im = Image.open(src)
    base = im.info.get("duration", 100) or 100
    step, dur = (2, base * 2) if base < 60 else (1, base)   # thin out very fast GIFs
    max_frames = max(12, MOTION_MS // dur)
    frames = []
    for i, frame in enumerate(ImageSequence.Iterator(im)):
        if i % step:
            continue
        frame = frame.convert("RGB")
        w, h = frame.size
        frames.append(frame.resize((MOTION_WIDTH, round(h * MOTION_WIDTH / w)), Image.LANCZOS))
        if len(frames) >= max_frames:
            break
    frames[0].save(dst, "WEBP", save_all=True, append_images=frames[1:],
                   duration=dur, loop=0, quality=MOTION_QUALITY, method=6)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="rebuild files that already exist")
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    args = ap.parse_args()

    os.makedirs(THUMB_DIR, exist_ok=True)
    os.makedirs(MOTION_DIR, exist_ok=True)

    built = skipped = missing = 0

    for coll in COLLECTIONS:
        d = os.path.join(ROOT, coll)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md"):
                continue
            path = os.path.join(d, name)
            text = open(path, encoding="utf-8").read()

            teaser = field(text, "teaser")
            if not teaser:
                continue

            src = os.path.join(ROOT, teaser.lstrip("/"))
            if not os.path.exists(src):
                print(f"  MISSING SOURCE  {coll}/{name}  ->  {teaser}")
                missing += 1
                continue

            stem = os.path.splitext(os.path.basename(src))[0]
            is_gif = src.lower().endswith(".gif")

            thumb_rel = field(text, "thumb") or f"/images/thumbs/{stem}.jpg"
            thumb_abs = os.path.join(ROOT, thumb_rel.lstrip("/"))
            if args.force or not os.path.exists(thumb_abs):
                if args.check:
                    print(f"  would build     {thumb_rel}")
                else:
                    build_thumb(src, thumb_abs)
                    print(f"  thumb           {thumb_rel}  "
                          f"({os.path.getsize(thumb_abs)//1024} KB)")
                built += 1
            else:
                skipped += 1

            motion_rel = None
            if is_gif:
                motion_rel = field(text, "motion") or f"/images/motion/{stem}.webp"
                motion_abs = os.path.join(ROOT, motion_rel.lstrip("/"))
                if args.force or not os.path.exists(motion_abs):
                    if args.check:
                        print(f"  would build     {motion_rel}")
                    else:
                        build_motion(src, motion_abs)
                        print(f"  motion          {motion_rel}  "
                              f"({os.path.getsize(motion_abs)//1024} KB)")
                    built += 1
                else:
                    skipped += 1

            if args.check:
                continue

            updated = set_field(text, "thumb", thumb_rel, after="teaser")
            if motion_rel:
                updated = set_field(updated, "motion", motion_rel, after="thumb")
            if updated != text:
                open(path, "w", encoding="utf-8").write(updated)
                print(f"  front matter    {coll}/{name}")

    print(f"\n{'would build' if args.check else 'built'}: {built}   "
          f"up to date: {skipped}   missing sources: {missing}")
    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
