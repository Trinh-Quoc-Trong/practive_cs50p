def main() -> None:
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting: str) -> int:
    greeting_casefolded = greeting.casefold()
    if greeting_casefolded.startswith("hello"):
        return 0
    if greeting_casefolded.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()

