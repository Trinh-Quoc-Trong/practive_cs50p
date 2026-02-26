def main() -> None:
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(s: str) -> bool:
    if not (2 <= len(s) <= 6):
        return False

    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started:
                number_started = True
                if char == "0":
                    return False
        elif number_started:
            return False

    return True


if __name__ == "__main__":
    main()

