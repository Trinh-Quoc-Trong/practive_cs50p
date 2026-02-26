import sys


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Invalid usage")

    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(count_lines(file))
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(file) -> int:
    lines_of_code = 0
    for line in file:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        lines_of_code += 1
    return lines_of_code


if __name__ == "__main__":
    main()
