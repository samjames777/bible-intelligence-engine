import json
from pprint import pprint

with open("data/raw/holy_bible.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("ROOT TYPE:", type(data))

if isinstance(data, list):
    print("TOTAL BOOKS:", len(data))

    print("\nFIRST BOOK KEYS:")
    pprint(data[0].keys())

    print("\nFIRST BOOK NAME:")
    pprint(data[0])

elif isinstance(data, dict):
    print("TOP LEVEL KEYS:")
    pprint(data.keys())