import os

# One-line roast: the fridge's petty midnight rule, turned back on it.
# The lock is the joke — it guards my health at 00:00 but never once
# guarded the cake at 11:59.
ENTRY = "My fridge locks at midnight for my own good. Strange \u2014 it never once locked the cake away from me at 11:59."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
