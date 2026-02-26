import pytest

from numb3rs import validate


@pytest.mark.parametrize(
    "ip",
    [
        "0.0.0.0",
        "1.2.3.4",
        "192.168.0.1",
        "255.255.255.255",
    ],
)
def test_validate_accepts_valid(ip):
    assert validate(ip) is True


@pytest.mark.parametrize(
    "ip",
    [
        "256.0.0.1",
        "275.3.6.28",
        "255.255.255.256",
        "1.2.3",
        "1.2.3.4.5",
        "1.2.3.-1",
        "1.2.3.a",
        "cat",
        " 1.2.3.4",
        "1.2.3.4 ",
    ],
)
def test_validate_rejects_invalid(ip):
    assert validate(ip) is False

