from plates import is_valid


def test_length_rules() -> None:
    assert is_valid("AA") is True
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False


def test_starts_with_two_letters() -> None:
    assert is_valid("CS") is True
    assert is_valid("C1") is False
    assert is_valid("1C") is False


def test_only_alphanumeric() -> None:
    assert is_valid("CS50") is True
    assert is_valid("CS-50") is False
    assert is_valid("CS 50") is False
    assert is_valid("CS50!") is False


def test_numbers_at_end() -> None:
    assert is_valid("CS50") is True
    assert is_valid("CS5A") is False
    assert is_valid("AAA222") is True
    assert is_valid("AA22A") is False


def test_first_number_not_zero() -> None:
    assert is_valid("CS05") is False
    assert is_valid("CS0") is False
    assert is_valid("CS10") is True
