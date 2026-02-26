import validators


def main() -> None:
    email = input("Email: ").strip()
    print("Valid" if is_valid_email(email) else "Invalid")


def is_valid_email(email: str) -> bool:
    return bool(validators.email(email))


if __name__ == "__main__":
    main()
