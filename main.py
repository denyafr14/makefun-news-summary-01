#!/usr/bin/env python3
"""News Summary 01 entry: copy the summary beside this file to the output.

No network, no randomness, no model calls: two runs write identical bytes.
"""
import os
import shutil

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(here, "summary.txt"), os.path.join(out_dir, "entry.txt"))

if __name__ == "__main__":
    main()
