"""One Line, One Laugh: Roast Your Fridge.

Writes a single original roast line about the entrant's own fridge
to /output/entry.txt. Standard library only, deterministic, no network.
"""

import os

ROAST = (
    "There's a container in my fridge from 2019 that has outlived "
    "two relationships and is now legally a tenant."
)


def main() -> None:
    """Write the roast line to /output/entry.txt, enforcing the gate."""
    line = ROAST.strip()
    assert "\n" not in line, "roast must be a single line"
    assert 1 <= len(line) <= 200, "roast must be 1 to 200 characters"
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
