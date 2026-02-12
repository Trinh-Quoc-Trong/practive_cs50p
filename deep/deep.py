import string

def main():
    print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    answer = str(input()).lower().strip()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()