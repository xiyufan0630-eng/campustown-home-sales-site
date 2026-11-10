"""Writes data/city_median_sale_price.json: the median sale price for each city.

Reads data/college_town_home_sales.csv (read-only). Rule: sales under $10,000 are
left out, as are rows with a blank sale_price. Each city's median is computed from
the sales that remain.

Run from the repository root:
    python3 scripts/city_median_sale_price.py
"""
import csv
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "college_town_home_sales.csv"
OUTPUT = ROOT / "data" / "city_median_sale_price.json"
MIN_PRICE = 10_000  # the $10,000 rule

prices_by_city = {}
rows_by_city = {}
excluded_by_city = {}

with SOURCE.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        city = row["city"]
        state = row["state"]
        key = (city, state)
        rows_by_city[key] = rows_by_city.get(key, 0) + 1
        text = (row["sale_price"] or "").strip()
        if not text:
            excluded_by_city[key] = excluded_by_city.get(key, 0) + 1
            continue
        price = int(float(text))
        if price < MIN_PRICE:
            excluded_by_city[key] = excluded_by_city.get(key, 0) + 1
            continue
        prices_by_city.setdefault(key, []).append(price)

cities = []
for (city, state), prices in prices_by_city.items():
    cities.append({
        "city": city,
        "state": state,
        "rows_in_file": rows_by_city[(city, state)],
        "excluded_under_10000_or_blank": excluded_by_city.get((city, state), 0),
        "sales_used": len(prices),
        "median_sale_price": statistics.median(prices),
    })
cities.sort(key=lambda c: c["median_sale_price"], reverse=True)

result = {
    "source": "data/college_town_home_sales.csv",
    "rule": "Sales under $10,000 and blank sale prices are excluded.",
    "minimum_sale_price": MIN_PRICE,
    "measure": "Median of sale_price, in US dollars, per city.",
    "cities": cities,
}

with OUTPUT.open("w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
    f.write("\n")

print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(cities)} cities.")
for c in cities:
    print(f"{c['city']}, {c['state']}: rows {c['rows_in_file']}, used {c['sales_used']}, median {c['median_sale_price']:,.0f}")
