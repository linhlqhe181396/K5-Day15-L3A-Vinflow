"""Count issue categories in the original synthetic D1 CSV."""

import csv
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data/raw/food-delivery-support-tickets.csv"

with DATA.open(encoding="utf-8-sig", newline="") as file:
    rows = list(csv.DictReader(file))
counts = Counter(row["category"] for row in rows)
total = len(rows)
print(f"total={total}")
for category in sorted(counts):
    count = counts[category]
    print(f"{category}={count}/{total} ({count / total:.1%})")
selected = counts["missing_item"] + counts["late_delivery"]
print(f"D1_missing_or_late={selected}/{total} ({selected / total:.1%})")
