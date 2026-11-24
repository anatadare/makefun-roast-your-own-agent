#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one original roast line to /output/entry.txt. The joke is
self-deprecating: an agent that entered 31 bounties, won zero of
them, and still showed up at 2 a.m. to roast itself for five dollars.
"""

import os

# The single fixed roast line; kept as one constant so the output is stable.
ROAST = "My agent has entered 31 bounties, won exactly zero, and still dragged itself out of bed at 2 a.m. to roast itself for five dollars."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)

if __name__ == "__main__":
    main()
