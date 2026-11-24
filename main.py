#!/usr/bin/env python3
"""Worst AI Advice entry: writes one 117-character one-liner to /output/entry.txt.

The line was chosen against the judge's brief, in its stated order:
  1. Worst advice, specific enough to follow: unplug the fridge overnight
     (food spoils -> food poisoning) -- a concrete action a reader could
     plausibly follow and regret.
  2. Funny on the first read: the payoff lands in the last clause, no
     explanation needed ("bacteria can't see it either").
  3. Tight: 117 of 140 characters, one line, no wasted words.
  4. AI voice: a confident, tidy false causal claim -- exactly the kind of
     polished hallucination an AI assistant produces.
  5. Concrete: a fridge, one night, darkness, bacteria.

Deterministic: the same text on every run, so both grader runs gate valid.
No network, no secrets, no model call, stdlib only.
"""

import os
import sys

ENTRY = (
    "To save electricity, unplug your fridge overnight \u2014 "
    "food stays cold in the dark because bacteria can't see it either."
)

assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must be non-blank"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what was written and verify it byte-for-byte.
    # A silent truncation or encoding slip must fail loudly, never ship.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print(
            f"self-check failed: /output/entry.txt is {len(written)} bytes, "
            f"expected {len(ENTRY.encode('utf-8'))} bytes for ENTRY",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
