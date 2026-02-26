def main():
    input_text = input("Input: ")
    for char in input_text:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            print(char, end="")
    print()

if __name__ == "__main__":
    main()