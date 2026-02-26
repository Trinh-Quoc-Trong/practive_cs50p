import pytest

from fuel import convert, gauge


def test_convert_rounding() -> None:
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("99/100") == 99


def test_convert_raises_value_error() -> None:
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_raises_zero_division_error() -> None:
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_outputs() -> None:
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
