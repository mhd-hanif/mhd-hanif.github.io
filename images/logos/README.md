# Affiliation logos

Drop the files below into this directory and they will appear in the
Affiliations strip on the homepage automatically — no code or YAML change
needed. Until a file exists, that entry falls back to a typographic wordmark
tile, so a missing logo never renders as a broken image.

| File | Organisation | Status |
|---|---|---|
| `deepx.png` | DeepX, Inc. | in use |
| `science-tokyo.png` | Institute of Science Tokyo | in use |
| `mext.png` | MEXT Scholarship | in use |
| `iros-tech.jpg` | IROS Tech | in use |
| `itb.png` | Bandung Institute of Technology | in use |
| `tokyo-tech.png` | Tokyo Institute of Technology | spare — the pre-2024 mark, kept in case you want to show both eras |

These were produced from the files uploaded in `[Assets] Add affiliation logo`:
each was trimmed of surrounding whitespace, normalised to 160px tall and
re-encoded, taking the set from roughly 600 KB to 60 KB. The raw uploads were
removed once processed, since these supersede them; `git show 7e802a0` restores
them if ever needed.

The filenames are configured in `_data/affiliations.yml`; change them there if
you prefer different ones. `.svg` works too — update the extension in that file
to match.

## What to supply

- **Height:** around 200px is plenty. Logos are rendered at 44px tall and
  scaled down, so anything larger is wasted bytes.
- **Background:** transparent PNG or SVG is best. Logos sit on a light plate in
  both themes, so a white background is acceptable but transparent looks
  cleaner.
- **Cropping:** trim surrounding whitespace. Wordmarks (DeepX, Science Tokyo)
  and square marks (ITB, MEXT, IROS Tech) are both handled — the template
  fits by height and caps the width.

## A note on trademarks

These are third-party marks used to identify organisations you are genuinely
affiliated with, which is ordinary nominative use on a personal CV site. Use
each organisation's official logo file where possible rather than a redrawn or
recoloured version, and don't alter the colours or proportions.
