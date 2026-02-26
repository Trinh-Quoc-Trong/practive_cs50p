import random


def main():
    level = prompt_positive_int("Level: ")
    secret = random.randint(1, level)

    while True:
        guess = prompt_positive_int("Guess: ")
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break


def prompt_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            continue
        if value > 0:
            return value


if __name__ == "__main__":
    main()
