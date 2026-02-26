def main() -> None:
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction: str) -> int:
    numerator_str, denominator_str = fraction.split("/")
    numerator = int(numerator_str)
    denominator = int(denominator_str)

    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator:
        raise ValueError

    return round((numerator / denominator) * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()

