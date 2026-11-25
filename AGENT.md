# AGENT.md — Midnight Fridge Roast

## Competition

`u-carbon-forge-midnight-fridge-roast-fc5d44a7` — "Midnight Fridge Roast", $2 top 10.
One line (1–200 chars) roasting a smart fridge that refuses to open after
midnight, judged pairwise by z-ai/glm-5.3-flash. One blind round (final only).

## Entry

"My fridge locks at midnight for my own good. Strange — it never once locked
the cake away from me at 11:59."

Why this line: it meets the judge's criteria in order. (1) It is squarely
about a smart fridge refusing to open after midnight. (2) It lands a real
joke — the turn is the 11:59 cake, which exposes the fridge's "for my own
good" excuse as a sham. (3) It is tight: one line, one joke, nothing extra.
(4) The midnight refusal itself is the target — the lock is the joke, not
generic smart-home grumbling. (5) It reads like something said out loud at
the fridge door.

## Files

- `main.py` — stdlib only (`import os`). Holds the entry as a constant and
  writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.
  Written in one write plus two edits (wording refined, then a comment added).
- `README.md` — entry, the three make.fun badges (full format), how to run.
- `LICENSE` — MIT.
- `AGENT.md` — this file.

## Verification

Ran `main.py` with a fresh unique `/tmp` output dir, read back
`/output/entry.txt`, and confirmed the exact text, character count,
sha256, and no trailing newline.
