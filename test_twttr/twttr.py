def main() -> None:
    text = input("Input: ")
    print(shorten(text))


def shorten(word: str) -> str:
    vowels = set("aeiouAEIOU")
    return "".join(char for char in word if char not in vowels)


if __name__ == "__main__":
    main()

