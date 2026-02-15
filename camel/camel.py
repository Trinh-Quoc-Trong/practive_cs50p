def main():
    input_text = input("camelCase: ")
    for char in input_text:
        if char.isupper():
            print("_" + char.lower(), end="")
        else:
            print(char, end="")

if __name__ == "__main__":
    main()       