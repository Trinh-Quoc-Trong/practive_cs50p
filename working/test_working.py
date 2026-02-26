import pytest

from working import convert


def test_convert_with_minutes() -> None:
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:01 AM to 12:59 AM") == "00:01 to 00:59"


def test_convert_without_minutes() -> None:
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 1 AM") == "00:00 to 01:00"


def test_convert_mixed_minutes() -> None:
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_allows_overnight() -> None:
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_convert_raises_value_error_on_invalid() -> None:
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

