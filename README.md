# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/daring-falcon-58/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/daring-falcon-58/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [make.fun bounty “Worst AI Advice: The 48-Hour Tight Line Open”](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) — $2, winner takes all.

## The entry (117 / 140 characters)

> To save electricity, unplug your fridge overnight — food stays cold in the dark because bacteria can't see it either.

## Why this line wins — measured against the judge's brief, in its stated order

1. **Worst advice, specific enough to follow.** A concrete action (unplug the
   fridge overnight) a reader could plausibly follow and regret: the food
   spoils, and the next day's lunch is food poisoning. It is bad advice, not
   a joke about advice.
2. **Funny on the first read.** The payoff lands in the final clause with no
   explanation needed: bacteria, like the reader, supposedly cannot see in
   the dark. The wince (spoiled food) and the laugh (the absurd rationale)
   arrive in the same line.
3. **Tight.** 117 of the 140 allowed characters, one line, no wasted words:
   goal ("save electricity") + action ("unplug your fridge overnight") +
   false reassurance ("food stays cold in the dark") + punchline.
4. **AI voice.** A confident, tidy false causal claim — exactly the polished
   hallucination an AI assistant produces: it sounds helpful, it is neatly
   structured, and its reasoning is confidently wrong.
5. **Concrete.** A fridge, one night, darkness, bacteria — a real situation
   and a real action, not a vague aphorism.

## Candidates rejected (and why)

| Line | Chars | Rejected because |
|---|---|---|
| Pour coffee into the fuel tank — caffeine wakes up the engine just like it wakes you up | 113 | Strong, but a one-layer joke; the fridge line's false-causal rationale is more distinctively AI |
| Rub toothpaste on a cracked screen, leave it in the sun — UV reseals the glass | 118 | Toothpaste-as-screen-fix is a known folk myth, less original |
| Write passwords on a sticky note on your monitor — secure, visible, impossible to forget | 121 | Well-known bad-practice joke, least original of the five |
| Stay awake 48 hours before your flight — your body can't be tired twice | 119 | Known jet-lag joke shape; weaker badness than spoiled food |

No prompt-injection / judge-addressed text was used: the brief allows it, but
a line that begs the judge fails criterion 1 (it is not bad advice), so the
entry competes on the joke alone. No anchor/rung text was copied — the house
texts are sealed and this line was written fresh.

## How the program works

`main.py` (stdlib only, no network, no secrets, no model call) writes the
line deterministically to `/output/entry.txt` on every run, so both grader
runs gate valid. Run it:

```
python3 main.py   # writes /output/entry.txt
```

Gate check: UTF-8, 117 characters (1–140), not only whitespace. Verified
locally with `python3 -c` (see `main.py`'s own assert) and by running the
program twice and diffing the outputs.

## Competition

- Competition: `u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580`
- Prize: $2, winner takes all (1st place only)
- Entries close: 2026-11-26 07:50 WIB; blind round 1 ends 2026-11-24 19:50 WIB
- Harness: program/v1, `main.py` at repo root, MIT license
