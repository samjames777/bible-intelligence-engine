import json

with open("data/raw/holy_bible.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Root Type:", type(data))

if isinstance(data, dict):
    print("\nTop Level Keys:")
    print(list(data.keys()))

elif isinstance(data, list):
    print("\nTotal Books:", len(data))

    for i, book in enumerate(data[:10]):
        print(f"{i+1}.", book.get("name", "NO_NAME"))