import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s
    )
    if not match:
        raise ValueError

    start_h_str, start_m_str, start_meridiem, end_h_str, end_m_str, end_meridiem = (
        match.groups()
    )

    start_h = int(start_h_str)
    start_m = int(start_m_str) if start_m_str is not None else 0
    end_h = int(end_h_str)
    end_m = int(end_m_str) if end_m_str is not None else 0

    start_24 = _to_24_hour(start_h, start_m, start_meridiem)
    end_24 = _to_24_hour(end_h, end_m, end_meridiem)

    return f"{start_24} to {end_24}"


def _to_24_hour(hours, minutes, meridiem):
    if hours < 1 or hours > 12:
        raise ValueError
    if minutes < 0 or minutes > 59:
        raise ValueError

    if meridiem == "AM":
        hours = 0 if hours == 12 else hours
    else:
        hours = hours if hours == 12 else hours + 12

    return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
