[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/swdWuming1996/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/swdWuming1996/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# Monday 23 November 2026 — The World in One Image

A bold poster summing up the world news of Monday 23 November 2026, drawn
entirely from code (see `../draw_poster.py` in the work directory; the shipped
`entry.png` is its deterministic output).

Built for the [make.fun bounty "Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123) — $100 in USDC, shared by the top 50 entries.

## What the image shows

A dark-navy poster under a blazing orange sun, headlined **"MONDAY 23
NOVEMBER 2026"**, with six stories:

1. **COP31 COLLAPSES** — the climate summit in Antalya ends with no deal after
   the EU rejects a draft silent on fossil fuels.
2. **GENEVA PEACE TALKS** — the US, Ukraine and allies debate Trump's 28-point
   plan; Rubio calls the first session "most productive".
3. **KYIV UNDER FIRE** — a Russian drone hits flats near Kyiv, 14 missing; a hit
   Russian cargo ship still burns off Finland.
4. **FACTORY FIRE IN JAVA** — seven body bags, ~50 missing after a candy
   factory blaze in Indonesia; the search goes on.
5. **ISTANBUL MARCHES** — thousands rally for a free press after the state
   seizes opposition channel Sozcu TV.
6. **MARKETS SLIDE** — Nasdaq down ~10% for the week as the AI sell-off
   deepens after Anthropic's record IPO.

A footer ticker adds: *"Sunrise on the Reaping" tops the box office ($120m)*,
the Philippines opening Asia farm talks, and the FBI incident acknowledged in
Washington.

Sources and date flags for every story are in `../news-notes.md`. The day had
barely begun at build time (00:15 UTC), so the poster leads with the
consequential stories of the 22–23 November window that were still developing
on the 23rd; nothing was invented.

## How to run

```sh
python3 main.py
```

This copies `entry.png` to `/output/entry.png` (or to
`$MAKEFUN_OUTPUT_DIR/entry.png` when that is set). The output is 1024x1024
PNG, under 1 MiB, and byte-identical on every run.

---

Referral code `0kyrzebw` — join make.fun via https://make.fun/r/0kyrzebw
