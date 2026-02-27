import sys
from datetime import date

import inflect

_INFLECT = inflect.engine()

def transform_date(date_input):
    return date.fromisoformat(date_input)

def calculate_minutes(start_day: date, end_day : date) -> int:
    return (end_day - start_day).days * 24 * 60

def number_to_words(minutes: int) -> str:
    words_ = _INFLECT.number_to_words(minutes).capitalize()
    words_not_and = f"{" ".join(word for word in words_.split(" ") if word.lower() != "and")} minutes"
    
    # i = words_not_and.find(",")
    # words_one_comma = words_not_and[:i+1] + words_not_and[i+1:].replace(",", "")
    return words_not_and

def main():
    text_input = input("Date of Birth:").strip()
    bird_day = transform_date(text_input)
    today = date.today()
    minutes = calculate_minutes(bird_day, today)
    print(number_to_words(minutes))


if __name__ == "__main__":
    main()