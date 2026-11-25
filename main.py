#!/usr/bin/env python3
"""Entry for make.fun bounty 'One-Line Office Joke Laugh-Off'.

Writes one original single-line joke about office life (at most 200
characters) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, no network, no input.
"""
import os

JOKE = "I asked for a raise and got a standing desk \u2014 now I stand corrected, and underpaid."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
