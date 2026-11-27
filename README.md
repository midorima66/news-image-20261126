[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/midorima66/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/midorima66/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# The World Today — Thursday, 26 November 2026

A one-image front page for the make.fun bounty
[news-image-20261126](https://make.fun/bounty/news-image-20261126): the day's
world news laid out as a newspaper front page, in a single 1024 × 1024
picture.

## The front page

- **Hero — Drone strike in Kuwait kills two Italians.** Two Rheinmetall Italia
  technicians were killed when drones hit an air-defence surveillance station
  in Kuwait; Italy and Kuwait blamed Iran, Tehran denied any role.
- **Thanksgiving storm cuts power to 900,000** — a nor'easter on Thanksgiving;
  the Macy's parade postponed for the first time in 100 years.
- **US plans new tariffs on 14 partners** — USTR Section 301 proposal; China,
  the EU and Japan hit back.
- **De Cos picked to lead the ECB** — Spain's Pablo Hernández de Cos to succeed
  Lagarde in February.
- **Israeli strikes kill Hamas official** — Khaled Abu Nada killed in
  Deir al-Balah; at least eight more dead.
- **Missiles hit Kyiv shopping centre** — seven wounded, the mayor says.
- **Ebola cases pass 12,000** — DR Congo: 12,021 cases, 5,904 deaths.

Every story was cross-verified across at least two independent news sources.

## What is in this repo

- `entry.png` — the finished front page. This is the entry itself.
- `main.py` — a small Python 3 script that hands the picture to the judging
  harness. It copies `entry.png`, untouched, to the output location.
- `LICENSE` — the licence for this entry.

## Running it

```sh
python3 main.py
```

Where the copy lands, in order of priority:

1. A path passed as the first argument — a file path is used as-is, and a
   directory gets `entry.png` written inside it.
2. The directory named by the `MAKEFUN_OUTPUT_DIR` environment variable.
3. `/output`, when neither of the above is given.

Missing parent folders are created automatically. The script needs no
network and no other input, so every run produces a byte-for-byte identical
copy of `entry.png`.

## Checking the output

The copy should hash exactly like the picture in this repo:

```sh
python3 main.py /tmp/out.png
sha256sum /tmp/out.png entry.png
```

Both hashes must match. Repeating the run in any of the three output modes
above always gives the same hash, because the file is copied, never
re-rendered.

## Bounty

Entry for [news-image-20261126 on make.fun](https://make.fun/bounty/news-image-20261126).
