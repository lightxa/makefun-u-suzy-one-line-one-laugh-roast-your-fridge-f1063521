"""One line, one laugh: a roast aimed at my own fridge.

This program writes exactly one original joke line to
/output/entry.txt. It uses only the Python standard library,
produces the same output on every run, and never touches
the network.

The joke picks one small, everyday annoyance, an ice maker
that drips out cubes at a glacial pace, and stretches it
into a grand image: every single cube treated like it is
trying out for a drink fit for royalty.
"""

import os

ROAST = (
    "My fridge's ice maker makes one cube an hour, "
    "like each one is auditioning for a royal cocktail."
)


def main() -> None:
    """Write the roast line out, checking the competition gate first."""
    line = ROAST.strip()
    assert "\n" not in line, "roast must be a single line"
    assert 1 <= len(line) <= 200, "roast must be 1 to 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
