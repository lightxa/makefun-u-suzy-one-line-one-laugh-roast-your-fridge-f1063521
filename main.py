"""One Line, One Laugh: Roast Your Fridge.

Writes a single original roast line about the entrant's own fridge
to /output/entry.txt. Standard library only, deterministic, no network.

The roast targets one specific, recognisable detail: the ice maker,
which produces cubes so slowly that each one feels hand-made for
someone important. The twist lands in the last few words.
"""

import os

ROAST = (
    "My fridge's ice maker makes one cube an hour, "
    "like each one is auditioning for a royal cocktail."
)


def main() -> None:
    """Write the roast line to /output/entry.txt, enforcing the gate."""
    line = ROAST.strip()
    assert "\n" not in line, "roast must be a single line"
    assert 1 <= len(line) <= 200, "roast must be 1 to 200 characters"
    os.makedirs("/output", exist_ok=True)
    open("/output/entry.txt", "w", encoding="utf-8").write(line)


if __name__ == "__main__":
    main()
