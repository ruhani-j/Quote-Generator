import random
import time

# Load quotes from file
quotes = []
with open("quotes.txt", "r") as f:
    # category|quote|source|extra
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
        
# Collect all unique categories
categories = sorted(set(q["category"] for q in quotes if q["category"]))

# Initialize sorted_quotes to all quotes by default
sorted_quotes = quotes[:]

while True:
    # Menu
    print("\nQuote Generator")
    print("1. Show a random quote")
    print("2. Show random quote by category")
    print("3. Show all categories")
    print("4. Print all quotes")
    print("5. Sort quotes") 
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Completely random quote
        q = random.choice(quotes)
        display = f'"{q["text"]}"'
        if q["source"]:
            display += f" — {q['source']}"
        if q["extra"]:
            display += f" ({q['extra']})"
        print(display)
        
    if choice == "2":
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
            
    elif choice == "3":
        print("Available categories:")
        for cat in categories:
            print(f"- {cat}")
            
    elif choice == "4":
        # Print all quotes neatly
        for q in sorted_quotes:
            display = f'"{q["text"]}"'
            if q["source"]:
                display += f" — {q['source']}"
            if q["extra"]:
                display += f" ({q['extra']})"
            print(display)
     
    elif choice == "5":
        print("Sort quotes by:")
        print("1. Category")
        print("2. Source")
        sort_choice = input("Enter your choice: ")

        if sort_choice == "1":
            sorted_quotes = sorted(quotes, key=lambda q: q["category"])
        elif sort_choice == "2":
            sorted_quotes = sorted(quotes, key=lambda q: q["source"])
        else:
            print("Invalid choice. Keeping previous order.")
            sorted_quotes = quotes
        print("Quotes sorted!")
            
    elif choice == "6":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Goodbye!")
        break
    
    time.sleep(3)  # pauses for 3 seconds so user can read the quote before being prompted again
