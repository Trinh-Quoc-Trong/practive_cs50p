def main():
    input_ = input("Expression: ").strip().split(" ")
    first_number = float(input_[0])
    operator = input_[1]
    second_number = float(input_[2])
    
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    else:
        print("Does not compute")

if __name__ == "__main__":
    main()
