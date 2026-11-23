# SPDX-License-Identifier: MIT
"""Write one short, intriguing text to /output/entry.txt.

The text is built to leave a reader curious in a calm way: a concrete,
gentle scene, a quiet impossibility at its centre, and a final image
that stays open instead of resolving. A librarian finds a warm book she
never shelved; the book tells the story of a reader finding that very
book, up to the line being read; the next page is blank except for one
small, fresh footprint in ink.
"""
import os

OPENING = "On the last shelf, the librarian found a book she had never shelved, "
MIDDLE = "its pages still warm. It told, in soft, plain words, the story of a "
TURN = "reader finding this book \u2014 up to this line. "
BLANK_PAGE = "The next page was blank, "
FOOTPRINT = "except for one small, fresh footprint in ink."

# The order matters: scene, impossibility, self-reference, blank page,
# and only then the footprint that refuses to explain itself.
TEXT = OPENING + MIDDLE + TURN + BLANK_PAGE + FOOTPRINT


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
