"""Write an original short poem about permission to /output/entry.txt.

Offline, standard library only. Compatible with Python 3.12 / 3.13.
"""

from pathlib import Path

POEM = """You lent me your keys,
not your house.
I water the plants;
I do not move the walls.

I knock anyway, key in hand.
One night you said no;
I never tried the handle.
Key cold in my pocket,
rain down my neck.

Now it rests in your palm,
warm, uncopied —
one key, returned whole."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
