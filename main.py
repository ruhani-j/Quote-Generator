import random
import time
import msvcrt

# Load quotes from file
quotes = []
with open("quotes.txt", "r", encoding="utf-8") as f:
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
    print("2. Show all categories")
    print("3. Show random quote by category")
    print("4. Add a new quote")
    print("5. Sort quotes")
    print("6. Print all quotes")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Completely random quote
        q = random.choice(quotes)
        display = f'"{q["text"]}"'
        if q["source"]:
            display += f" — {q['source']}"
        if q["extra"]:
            display += f" ({q['extra']})"
        print(display.replace("\\n", "\n"))  # Make \n display as actual new line
        
    elif choice == "3":
        cat = input("Enter category: ").lower()
        filtered = [q for q in quotes if q["category"] == cat]
        if filtered:
            q = random.choice(filtered)
            display = f'"{q["text"]}"'
            if q["source"]:
                display += f" — {q['source']}"
            if q["extra"]:
                display += f" ({q['extra']})"
            print(display.replace("\\n", "\n"))  # Make \n display as actual new line
        else:
            print("No quotes in that category.")
            
    elif choice == "2":
        print("Available categories:")
        for cat in categories:
            print(f"- {cat}")
            
    elif choice == "4":
        # Add new quote locally
        new_category = input("Enter category: ").strip()
        new_text = input("Enter quote text: ").strip()
        new_source = input("Enter source (optional): ").strip()
        new_extra = input("Enter extra info (optional): ").strip()
        quotes.append({
            "category": new_category.lower(),
            "text": new_text,
            "source": new_source,
            "extra": new_extra
        })
        sorted_quotes = quotes[:]
        if new_category.lower() not in categories:
            categories.append(new_category.lower())
            categories.sort()
        # Save to local file
        with open("quotes.txt", "a", encoding="utf-8") as f:
            f.write(f"{new_category}|{new_text}|{new_source}|{new_extra}\n")
        print("Quote added successfully!")
            
    elif choice == "6":
        # Print all quotes neatly
        for q in sorted_quotes:
            display = f'"{q["text"]}"'
            if q["source"]:
                display += f" — {q['source']}"
            if q["extra"]:
                display += f" ({q['extra']})"
            print(display.replace("\\n", "\n"))  # Make \n display as actual new line
     
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
            
    elif choice == "7":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        continue  # loops back to menu
    
    # Wait up to 3 seconds, exit early if Enter is pressed
    start = time.time()
    while True:
        if msvcrt.kbhit():  # key was pressed
            if msvcrt.getwch() == '\r':  # Enter key
                break
        if time.time() - start > 3:
            break
        time.sleep(0.05)  # small sleep to avoid busy wait
