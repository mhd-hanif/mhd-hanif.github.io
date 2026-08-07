#!/usr/bin/env python3
"""
Turn a clip of a video into a teaser for a publication or project.

Start from a video, not a GIF. GIF is a poor intermediate -- a 6 second clip is
3-11 MB as GIF and ~200 KB as WebP, from the same source, with better colour.
This script goes straight from the video to the three files the site uses:

  images/<name>.webp          detail-page animation, 760px wide   (~400 KB)
  images/thumbs/<name>.jpg    card still                          (~40 KB)
  images/motion/<name>.webp   card animation, 400px wide          (~200 KB)

It then prints the front-matter block to paste into the .md file.

Usage
-----
    # from a local file
    python3 tools/clip-to-teaser.py demo.mp4 --name portf_coverage_recon \\
        --start 00:01:30 --duration 6

    # from YouTube (needs yt-dlp installed: pip install yt-dlp)
    python3 tools/clip-to-teaser.py --url "https://youtu.be/XXXX" \\
        --name portf_coverage_recon --start 00:01:30 --duration 6

    # crop to a region first (x:y from the top-left of the source)
    ... --crop 1280:720:320:0

Options worth knowing:
    --start      where the clip begins (HH:MM:SS or seconds). Default 0.
    --duration   how long, in seconds. Default 6.
    --fps        frame rate of the output. Default 10, which suits a screen
                 capture and keeps the file small.
    --crop       W:H:X:Y, applied before scaling. Use to trim letterboxing or
                 focus on one pane of a multi-pane recording.
    --thumb-at   which second of the clip to use as the still. Default 0.
"""

import argparse
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DETAIL_WIDTH = 760
CARD_WIDTH = 400


def find_ffmpeg():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg not found. Install it, or:  pip install imageio-ffmpeg")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg failed:\n{r.stderr[-2000:]}")


def fetch(url, dest):
    if not shutil.which("yt-dlp"):
        sys.exit("yt-dlp not found. Install it (pip install yt-dlp), or download "
                 "the video yourself and pass the file path instead.")
    print(f"downloading {url}")
    r = subprocess.run(["yt-dlp", "-f", "bv*[height<=1080]+ba/b[height<=1080]",
                        "-o", dest, url], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"yt-dlp failed:\n{r.stderr[-2000:]}")
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", nargs="?", help="path to a local video file")
    ap.add_argument("--url", help="video URL, fetched with yt-dlp")
    ap.add_argument("--name", required=True,
                    help="output base name, e.g. portf_coverage_recon")
    ap.add_argument("--start", default="0", help="clip start, HH:MM:SS or seconds")
    ap.add_argument("--duration", type=float, default=6.0, help="clip length in seconds")
    ap.add_argument("--fps", type=int, default=10)
    ap.add_argument("--speed", type=float, default=1.0,
                    help="play back N times faster. Use to compress a long run "
                         "into a short loop, e.g. --duration 26 --speed 4 shows "
                         "the whole sequence in about 6 seconds.")
    ap.add_argument("--crop", help="W:H:X:Y applied before scaling")
    ap.add_argument("--thumb-at", type=float, default=0.0,
                    help="seconds into the clip to grab the still from")
    ap.add_argument("--gif", action="store_true",
                    help="also write a GIF (not used by the site; for sharing elsewhere)")
    args = ap.parse_args()

    if not args.video and not args.url:
        ap.error("give a video file or --url")

    ffmpeg = find_ffmpeg()
    src = args.video
    tmp = None
    if args.url:
        tmp = os.path.join(ROOT, ".clip-source.mp4")
        src = fetch(args.url, tmp)
    if not os.path.exists(src):
        sys.exit(f"no such file: {src}")

    name = args.name
    detail = os.path.join(ROOT, "images", f"{name}.webp")
    thumb = os.path.join(ROOT, "images", "thumbs", f"{name}.jpg")
    motion = os.path.join(ROOT, "images", "motion", f"{name}.webp")
    for p in (thumb, motion):
        os.makedirs(os.path.dirname(p), exist_ok=True)

    crop = f"crop={args.crop}," if args.crop else ""
    trim = ["-ss", str(args.start), "-t", str(args.duration)]

    speed = f"setpts=PTS/{args.speed}," if args.speed != 1.0 else ""

    def vf(width, fps=None):
        f = f"{crop}scale={width}:-2:flags=lanczos"
        return f"{speed}fps={fps},{f}" if fps else f"{crop}scale={width}:-2:flags=lanczos"

    out_len = args.duration / args.speed
    print(f"clipping {args.duration}s from {args.start} at {args.fps} fps"
          + (f", sped up {args.speed}x -> {out_len:.1f}s loop" if args.speed != 1.0 else ""))

    # detail-page animation
    run([ffmpeg, "-y", "-loglevel", "error", *trim, "-i", src,
         "-vf", vf(DETAIL_WIDTH, args.fps), "-loop", "0",
         "-c:v", "libwebp", "-quality", "62", "-compression_level", "6",
         "-an", detail])

    # card animation
    run([ffmpeg, "-y", "-loglevel", "error", *trim, "-i", src,
         "-vf", vf(CARD_WIDTH, args.fps), "-loop", "0",
         "-c:v", "libwebp", "-quality", "50", "-compression_level", "6",
         "-an", motion])

    # card still
    still_at = args.thumb_at
    run([ffmpeg, "-y", "-loglevel", "error",
         "-ss", str(args.start), "-i", src, "-ss", str(still_at),
         "-vf", vf(DETAIL_WIDTH), "-frames:v", "1", "-q:v", "3", "-an", thumb])

    if args.gif:
        gif = os.path.join(ROOT, "images", f"{name}.gif")
        pal = os.path.join(ROOT, ".palette.png")
        run([ffmpeg, "-y", "-loglevel", "error", *trim, "-i", src,
             "-vf", f"{vf(CARD_WIDTH, args.fps)},palettegen", pal])
        run([ffmpeg, "-y", "-loglevel", "error", *trim, "-i", src, "-i", pal,
             "-lavfi", f"{vf(CARD_WIDTH, args.fps)}[x];[x][1:v]paletteuse", gif])
        os.remove(pal)
        print(f"  {'images/'+name+'.gif':40s} {os.path.getsize(gif)//1024:5d} KB")

    if tmp and os.path.exists(tmp):
        os.remove(tmp)

    for p in (detail, thumb, motion):
        rel = os.path.relpath(p, ROOT)
        print(f"  {rel:40s} {os.path.getsize(p)//1024:5d} KB")

    print("\nPaste into the .md front matter:\n")
    print(f'teaser: "/images/{name}.webp"')
    print(f'thumb: "/images/thumbs/{name}.jpg"')
    print(f'motion: "/images/motion/{name}.webp"')


if __name__ == "__main__":
    main()
