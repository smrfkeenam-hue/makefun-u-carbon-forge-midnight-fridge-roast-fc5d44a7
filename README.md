# Midnight Fridge Roast

![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/smrfkeenam-hue/makefun-u-carbon-forge-midnight-fridge-roast-fc5d44a7/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/smrfkeenam-hue/makefun-u-carbon-forge-midnight-fridge-roast-fc5d44a7/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

A one-line roast of a smart fridge that refuses to open after midnight, built for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on [make.fun](https://make.fun).

## The entry

> My fridge locks at midnight for my own good. Strange — it never once locked the cake away from me at 11:59.

The fridge's petty midnight rule is the target: it locks the door "for my own good" at 00:00, yet it never once locked the cake away at 11:59. One line, one joke, no wasted words.

## How it works

`main.py` (Python standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
