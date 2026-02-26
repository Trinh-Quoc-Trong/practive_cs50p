def main():
    month_map = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }

    while True:
        date_str = input("Date: ").strip()

        month = day = year = None

        if "/" in date_str:
            parts = [p.strip() for p in date_str.split("/")]
            if len(parts) != 3:
                continue
            try:
                month, day, year = (int(parts[0]), int(parts[1]), int(parts[2]))
            except ValueError:
                continue
        else:
            if "," not in date_str:
                continue
            left, year_str = date_str.split(",", 1)
            left_parts = left.strip().split()
            if len(left_parts) != 2:
                continue
            month_name, day_str = left_parts[0].lower(), left_parts[1]
            if month_name not in month_map:
                continue
            try:
                month = month_map[month_name]
                day = int(day_str)
                year = int(year_str.strip())
            except ValueError:
                continue

        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year:04d}-{month:02d}-{day:02d}")
        break


if __name__ == "__main__":
    main()
