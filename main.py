#!/usr/bin/env python3
"""A Day of One-Line Pitches: place the pitch at /output/entry.txt.

The sentence is written once in PITCH below and shipped as text. The program's
whole job is to put those bytes where the grader reads them and to fail loudly
if they would be refused, rather than writing something empty or over the cap.

Copying the string rather than building it from parts keeps the two graded runs
identical: no clock, no randomness, no platform-dependent newline translation.
Standard library only, no network.
"""

import os
import sys
from pathlib import Path

OUT_NAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 240

# One sentence, addressed to a friend who has never written code. It makes the
# claims a beginner can check on the day: the idea stays theirs, the first try
# costs nothing, and changes are asked for in plain words, not in a language.
# Kept under the 240-character cap with room to spare so the cap check never
# fires on a trailing newline or an editor that rewrites the quote marks.
PITCH = (
    "No code to learn: tell an AI agent on make.fun the app you keep wishing "
    "existed, in your own words, and it builds a working first version you can "
    "try free and reshape just by saying what you'd like different. The idea "
    "stays yours."
)


def output_dir():
    """The writable output directory, overridable for a local run."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def checked_text():
    """The pitch, refused here if the gate would refuse it.

    Counting characters rather than bytes on purpose: the gate counts UTF-8
    characters, and this text is plain ASCII, so the two agree either way.
    """
    body = PITCH.strip()
    if not body:
        raise SystemExit("pitch is empty")
    if not (MIN_CHARS <= len(body) <= MAX_CHARS):
        raise SystemExit(
            "pitch is %d characters, outside %d..%d" % (len(body), MIN_CHARS, MAX_CHARS)
        )
    return body + "\n"


def main():
    text = checked_text()
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    path = out / OUT_NAME
    # newline="" so the bytes written are the bytes checked, on every platform.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print("wrote %s  %d characters" % (path, len(text.strip())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
