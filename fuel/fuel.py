def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break

    print(gauge(percentage))

def convert(fraction):
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0 or x > y:
        raise ValueError
    return int(round(x / y * 100))

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"  
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
