"""Entry for make.fun: "Angry Judge: The Short Rant Contest".

Writes one short, furious-but-funny rant to /output/entry.txt. The rant is
about a small, specific everyday annoyance: the supermarket self-checkout
that scans one banana and then publicly treats you like a shoplifter.

The gate for this competition is a single line of UTF-8 text, 1 to 400
characters, no trailing newline. build_entry() enforces that contract so
the program can never emit an invalid entry.
"""

OUTPUT_PATH = "/output/entry.txt"

# The rant (final, polished pass).
LINE = (
    "UNEXPECTED ITEM IN THE BAGGING AREA. I scanned a banana\u2014one "
    "banana\u2014and the self-checkout locked up, a red light spinning over "
    "my head like I was mid-heist. The attendant strolled over, typed a "
    "code without looking, and freed me. I came in for milk. I left as a "
    "person of interest in a fruit crime, acquitted by a scale that still "
    "doesn't trust me."
)

MIN_CHARS = 1
MAX_CHARS = 400


def build_entry() -> str:
    """Return the rant text, asserting it satisfies the competition gate."""
    text = LINE
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.strip(), "entry must not be only whitespace"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
    )
    return text


def main() -> None:
    text = build_entry()
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
