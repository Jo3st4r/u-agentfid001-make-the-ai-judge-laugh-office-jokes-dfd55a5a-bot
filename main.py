#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes a single one-line office joke (under 200 characters) to
/output/entry.txt. Stdlib only; no network, no randomness, no I/O
besides the one output file.

The joke is built from three named beats so each turn of the gag is
visible in the code:

* SETUP — the premise: my out-of-office reply does my job.
* ESCALATION — the comparison: it does it better than I do.
* PUNCH — the twist: HR wants to promote the auto-reply, not me.

My out-of-office reply now does my job better than I do, so HR
wants to promote it.
"""

import os

# The three beats of the joke, joined in entry_text().
SETUP = "My out-of-office reply now does my job"
ESCALATION = "better than I do"
PUNCH = "so HR wants to promote it."

# The competition caps the entry at 200 characters; the joke is 83.
MAX_CHARS = 200

ENTRY = "My out-of-office reply now does my job better than I do, so HR wants to promote it."


def entry_text() -> str:
    """Join the three beats into the one-line joke."""
    return f"{SETUP} {ESCALATION}, {PUNCH}"


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and exactly one line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge checks: the joke itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined line drifted from the entry joke"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
