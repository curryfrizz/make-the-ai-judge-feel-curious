# SPDX-License-Identifier: MIT
"""Write one short, intriguing text to /output/entry.txt.

The text is built to leave a reader curious in a calm way: a concrete,
gentle scene, a quiet impossibility at its centre, and a final image
that stays open instead of resolving.
"""
import os

TEXT = (
    "On the last shelf, the librarian found a book she had never shelved, "
    "its pages still warm. It told, in soft, plain words, the story of a "
    "reader finding this book \u2014 up to this line. The next page was blank, "
    "except for one small, fresh footprint in ink."
)


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
