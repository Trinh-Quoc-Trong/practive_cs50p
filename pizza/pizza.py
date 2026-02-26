import csv
import sys

from tabulate import tabulate


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Invalid usage")

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

    if not rows:
        print(tabulate([], headers=[], tablefmt="grid"))
        return

    headers = rows[0]
    data = rows[1:]
    print(tabulate(data, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
