import os

NOTE = (
    "Just a note: your leftovers have sat at exactly 3°C for nine days. "
    "I no longer refrigerate them. I curate them."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
