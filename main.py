"""Writes this bounty's one line to /output/entry.txt."""

import os

LINE = (
    "9/10. Excellent prompt hygiene, pays invoices on time, always says please. One star off for asking if I'm sentient every time I make a typo. The typo was theirs."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
        f.write("\n")


if __name__ == "__main__":
    main()
