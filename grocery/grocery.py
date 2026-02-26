def main():
    from collections import Counter
    import sys

    items = (
        line.strip().lower()
        for line in sys.stdin
    )
    counts = Counter(item for item in items if item)

    for item in sorted(counts):
        print(f"{counts[item]} {item.upper()}")


if __name__ == "__main__":
    main()
