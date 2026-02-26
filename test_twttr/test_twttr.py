from twttr import shorten


def test_lowercase_vowels() -> None:
    assert shorten("twitter") == "twttr"


def test_uppercase_vowels() -> None:
    assert shorten("TWITTER") == "TWTTR"


def test_mixed_case() -> None:
    assert shorten("TwItTeR") == "TwtTR"


def test_numbers_unchanged() -> None:
    assert shorten("CS50") == "CS50"


def test_punctuation_unchanged() -> None:
    assert shorten("Hello, world!") == "Hll, wrld!"


def test_no_vowels() -> None:
    assert shorten("rhythm") == "rhythm"


def test_empty_string() -> None:
    assert shorten("") == ""
