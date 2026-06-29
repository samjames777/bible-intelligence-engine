from pathlib import Path
import csv
import re

USFM_DIR = Path("data/raw/usfm")
OUTPUT_FILE = Path("data/processed/new_testament_verses.csv")

NT_FILES = [
    f for f in USFM_DIR.glob("*.usfm")
    if int(f.name[:2]) >= 41
]

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

rows = []

for file in sorted(NT_FILES):

    book_code = file.name.split("_")[1][:3]

    current_chapter = None

    with open(file, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if line.startswith("\\c "):
                current_chapter = line.replace("\\c ", "").strip()

            elif line.startswith("\\v "):

                match = re.match(r"\\v\s+(\d+)\s+(.*)", line)

                if match:

                    verse_num = match.group(1)
                    verse_text = match.group(2).strip()

                    rows.append([
                        book_code,
                        current_chapter,
                        verse_num,
                        verse_text
                    ])

with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "book_code",
        "chapter",
        "verse",
        "text_ml"
    ])

    writer.writerows(rows)

print(f"Total verses extracted: {len(rows)}")
print(f"Output file: {OUTPUT_FILE}")