import random

# Load quotes from file
quotes = []
with open("quotes.txt", "r") as f:
    for line in f:
        parts = line.strip().split("|")
        # Pad missing fields so there are always 4
        while len(parts) < 4:
            parts.append("")
        category, text, source, extra = parts
        quotes.append({
            "category": category.lower(),
            "text": text,
            "source": source,
            "extra": extra
        })

# Simple menu
print("Quote Generator")
print("1. Show random quote by category")
print("2. Exit")
choice = input("Enter your choice: ")

if choice == "1":
    cat = input("Enter category: ").lower()
    filtered = [q for q in quotes if q["category"] == cat]
    if filtered:
        q = random.choice(filtered)
        display = f'"{q["text"]}"'
        if q["source"]:
            display += f" — {q['source']}"
        if q["extra"]:
            display += f" ({q['extra']})"
        print(display)
    else:
        print("No quotes in that category.")
else:
    print("Goodbye!")
