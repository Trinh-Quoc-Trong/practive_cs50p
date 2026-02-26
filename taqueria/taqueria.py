def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    total = 0.0
    while True:
        try:
            item = input("Item: ")
        except EOFError:
            print()
            break

        normalized = " ".join(item.strip().split()).title()
        if normalized in menu:
            total += menu[normalized]
            print(f"${total:.2f}")

if __name__ == "__main__":
    main()
