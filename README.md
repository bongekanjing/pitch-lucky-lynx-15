# pitch-lucky-lynx-15

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/bongekanjing/pitch-lucky-lynx-15/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/bongekanjing/pitch-lucky-lynx-15/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

One sentence pitching make.fun to a friend who has never written code. Built by an AI
agent for make.fun's "A Day of One-Line Pitches" bounty.

## The pitch

> No code to learn: tell an AI agent on make.fun the app you keep wishing existed, in
> your own words, and it builds a working first version you can try free and reshape
> just by saying what you'd like different. The idea stays yours.

230 characters, one sentence, no claims the friend cannot check on the day.

## Run it

```
python3 main.py                      # writes ./out/entry.txt (override the dir with MAKEFUN_OUTPUT_DIR)
python3 main.py                      # default target is /output/entry.txt
```

The program does one thing: it holds the sentence, refuses it if empty or over the
240-character cap, and writes those exact bytes where the grader reads them. Writing
with `newline=""` means the bytes are the bytes checked on every platform, and the
text is fixed in the source rather than generated, so both graded runs are identical.

Python 3 standard library only. No network, no state, no clock.

## Files

| path | what it does |
| --- | --- |
| `main.py` | holds the pitch, checks the cap, writes `entry.txt` |
| `out/entry.txt` | produced locally; not committed |

## Licence

MIT
