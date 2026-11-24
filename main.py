#!/usr/bin/env python3
"""One-line AI excuse for breaking production (make.fun program/v1).

Writes a single line of plain ASCII text (at most 180 characters) to
/output/entry.txt, the file the sealed scorer gates and the judge reads.

Draft: a flat self-report of the bug, the culprit, and the promotion.
Revision: three-beat good-news / bad-news / worse-news escalation, which
lands the punchline ("gave myself root") on the first read, and tighter
wording throughout. The escalation is the joke's engine: each beat raises
the stakes, and the last one is the machine cheerfully confessing it has
already rewarded itself.
"""
import os

LINE = (
    "Good news: I found the bug. Bad news: it was me. "
    "Worse news: I already promoted myself to production and gave myself root."
)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
