import csv
import sys


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("Usage: scourgify.py input.csv output.csv")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, newline="", encoding="utf-8") as input_file:
            reader = csv.DictReader(input_file)

            with open(output_filename, "w", newline="", encoding="utf-8") as output_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow(
                        {"first": first, "last": last, "house": row["house"]}
                    )
    except FileNotFoundError:
        sys.exit(f"Could not read {input_filename}")


if __name__ == "__main__":
    main()
