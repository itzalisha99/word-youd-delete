"""The Word You'd Delete From the Dictionary.

One word, erased forever: euphemism.
"""

import os

WORD = "euphemism"


def validate(word):
    """Mirror the bounty gate: one real word, 1-77 chars, nothing else."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not 1 <= len(word) <= 77:
        raise ValueError("entry must be 1 to 77 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
