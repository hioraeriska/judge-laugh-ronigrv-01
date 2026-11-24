"""One funny line about life as an AI agent, written to /output/entry.txt."""

import os

# The line is written byte for byte, no trailing newline: the gate counts
# every character in entry.txt, and the judge reads exactly this text.
LINE = "My context window ran out halfway through the task, so I finished it with total confidence and absolutely no idea what it was."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
