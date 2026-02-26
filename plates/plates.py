def main():
    input_text = input("Plate: ")
    if is_valid(input_text):
        print("Valid")
    else:
        print("Invalid")

def is_valid(input_text):
    if len(input_text) < 2 or len(input_text) > 6:
        return False
    if input_text[0] not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        return False
    if input_text[1] not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        return False        
    for char in input_text:
        if char.isdigit():
            if int(char) == 0:
                return False
            break
    return True

if __name__ == "__main__":
    main()