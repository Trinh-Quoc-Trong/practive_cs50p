import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        if ask_problem(x, y):
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in (1, 2, 3):
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    raise ValueError("level must be 1, 2, or 3")


def ask_problem(x: int, y: int) -> bool:
    answer = x + y

    for attempt in range(3):
        try:
            guess = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            continue

        if guess == answer:
            return True

        print("EEE")

    print(f"{x} + {y} = {answer}")
    return False


if __name__ == "__main__":
    main()
