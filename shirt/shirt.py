import os
import sys

from PIL import Image, ImageOps


ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("Invalid usage")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in ALLOWED_EXTENSIONS or output_ext not in ALLOWED_EXTENSIONS:
        sys.exit("Invalid input")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    script_dir = os.path.dirname(__file__)
    shirt_path = os.path.join(script_dir, "shirt.png")

    try:
        with Image.open(input_path) as photo, Image.open(shirt_path) as shirt:
            fitted = ImageOps.fit(photo, shirt.size)
            fitted.paste(shirt, (0, 0), mask=shirt)
            fitted.save(output_path)
    except FileNotFoundError:
        sys.exit("File not found")
    except OSError:
        sys.exit("Invalid image")


if __name__ == "__main__":
    main()
