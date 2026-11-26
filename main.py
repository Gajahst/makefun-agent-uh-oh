"""The Agent's Uh-Oh: one word an agent blurts out when it has no idea what to do.

Writes the entry to /output/entry.txt.
"""
from pathlib import Path

WORD = "Uhbsolutely!"

# Hold the word to the gate before writing it: UTF-8, 1 to 99 characters,
# not only white space, and a single word (no spaces).
assert 1 <= len(WORD) <= 99, "entry must be 1 to 99 characters"
assert WORD.strip(), "entry must not be only white space"
assert " " not in WORD, "entry must be one word"
WORD.encode("utf-8")

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(WORD, encoding="utf-8")
print(WORD)
