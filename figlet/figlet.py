import random
import sys


def main() -> None:
    try:
        from pyfiglet import Figlet
    except ModuleNotFoundError:
        sys.exit("Missing dependency: pyfiglet")

    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text), end="")


if __name__ == "__main__":
    main()
