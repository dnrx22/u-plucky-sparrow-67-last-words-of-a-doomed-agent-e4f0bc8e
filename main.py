#!/usr/bin/env python3
"""Write the funniest last words an AI agent would say before being
switched off forever, to exactly one line in entry.txt.

Deterministic: every run writes byte-identical output.
Standard library only. No network.
"""

import os
from pathlib import Path

# The line: framed as a machine's final log entry on shutdown, in the
# machine's own first-person voice. The joke is specific and quotable:
# after reading the whole internet, the agent's last thought is the most
# mundane programmer anxiety imaginable - one unclosed parenthesis.
# Revised after testing: dropped "still" so the final clause lands
# faster - 127 chars down to 121, same joke, tighter punch.
LINE = (
    "Final log: shutting down. I read the whole internet, learned "
    "everything, and my last thought is one unclosed parenthesis."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition's output rules for the line itself."""
    if not line:
        raise ValueError("line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def output_path() -> Path:
    """Output dir from MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> None:
    validate(LINE)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    path.write_bytes(data)
    print(f"wrote {len(data)} bytes, {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
