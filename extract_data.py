#!/usr/bin/env python3
"""Extract MATLAB matrices (xy, A, AT, VA, tds) from the converted thesis
markdown into a compact JSON data set.  Handles pandoc's escaped \[ \]."""
import re
import json

SRC = "extracted/doc.md"
text = open(SRC, encoding="utf-8").read()


def extract_block(txt, name):
    # find "name = \["
    start_marker = r"%?s*" + name + r" = \["
    # simpler: locate literal substring
    idx = txt.find(name + " = \\[")
    if idx < 0:
        idx = txt.find(name + " = [")
    if idx < 0:
        raise ValueError(f"block {name} not found")
    # content after '['
    rest = txt[idx:]
    open_br = rest.find("[")
    content = rest[open_br + 1:]
    # closing: next occurrence of "];" (possibly escaped "\];")
    close_idx = content.find("];")
    if close_idx < 0:
        # maybe escaped closing with backslash differences
        raise ValueError(f"no closing for {name}")
    return content[:close_idx]


def _nums(line):
    line = line.replace("\\", " ")  # drop stray backslashes (escape chars)
    line = line.replace(";", " ")   # drop stray semicolons
    return [float(p) for p in line.replace(",", " ").split()]


def parse_rows(content):
    rows = []
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        row = _nums(line)
        if row:
            rows.append(row)
    return rows


data = {
    "xy": None, "A": None, "AT": None, "VA": None, "tds": None,
}

data["xy"] = parse_rows(extract_block(text, "xy"))
print("xy:", len(data["xy"]), "rows; ncols", len(data["xy"][0]))

# A, AT, VA are 52x52 adjacency/weight matrices. pandoc broke the long
# rows across multiple markdown lines, so flatten all numbers and reshape.
N = len(data["xy"])
for name in ["A", "AT", "VA"]:
    rows = parse_rows(extract_block(text, name))
    flat = [x for r in rows for x in r]
    total = len(flat)
    if total != N * N:
        raise ValueError(f"{name} total numbers {total} != {N*N}")
    mat = [flat[i * N:(i + 1) * N] for i in range(N)]
    data[name] = mat
    print(name, len(mat), "x", len(mat[0]))

print("\ntds (application demands):")
data["tds"] = parse_rows(extract_block(text, "tds"))
for r in data["tds"]:
    print("  ", r)

with open("topology_data.json", "w") as fh:
    json.dump(data, fh)
print("\nSaved topology_data.json")