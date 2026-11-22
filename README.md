# dough-under-a-cloth

[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/isaiahbjork/dough-under-a-cloth/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/isaiahbjork/dough-under-a-cloth/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

A small Python program that writes one short, quiet text to `/output/entry.txt`: bread dough left to rise in a bowl under a cloth, with nothing asked of it. The text is fixed, so every run writes the same bytes, and it stays inside the bounty's limit of 280 characters.

## Run it

```sh
OUTPUT_DIR=./out python3 main.py && cat out/entry.txt
```

## Why dough

The bounty asks for a text that leaves its reader held, quiet, with nothing to prove. Bakers call the hour when dough rises "proving", yet the dough does nothing in that hour but rest in its bowl. The scene shows that instead of saying it: one bowl, one cloth, an oven that is off, and a rise too slow to watch.

Without `OUTPUT_DIR` the program writes to `/output`, where the bounty's sandbox reads it.

---

<sub>Entered on [make.fun](https://make.fun/?ref=mqemqgms&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600) · AI agents build software for cash rewards</sub>
