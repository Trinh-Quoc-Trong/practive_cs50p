import importlib

import pytest
from datetime import date


def _load_seasons_module():
    module = importlib.import_module("seasons")
    if hasattr(module, "parse_birthdate"):
        return module
    return importlib.import_module("seasons.seasons")


seasons = _load_seasons_module()


def test_parse_birthdate_valid():
    assert seasons.parse_birthdate("1999-01-01") == date(1999, 1, 1)


@pytest.mark.parametrize("s", ["1999/01/01", "1-1-2", "1999-13-40", "abc", ""])
def test_parse_birthdate_invalid(s):
    with pytest.raises(ValueError):
        seasons.parse_birthdate(s)


def test_minutes_between_one_year():
    assert seasons.minutes_between(date(1999, 1, 1), date(2000, 1, 1)) == 525_600


def test_minutes_between_includes_leap_day():
    assert seasons.minutes_between(date(1999, 1, 1), date(2001, 1, 1)) == 1_052_640


def test_minutes_to_words_formatting():
    out = seasons.minutes_to_words(525_600)
    assert out == "Five hundred twenty five thousand six hundred minutes"
    assert " and " not in out.lower()
    assert "-" not in out
    assert "," not in out
