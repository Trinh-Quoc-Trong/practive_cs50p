def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
        except EOFError:
            print()
            break
        if name:
            names.append(name)

    joined = format_names(names)
    print(f"Adieu, adieu, to {joined}")


def format_names(names: list[str]) -> str:
    if not names:
        return ""

    try:
        import inflect  # type: ignore

        engine = inflect.engine()
        return engine.join(names)
    except ModuleNotFoundError:
        pass

    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()
