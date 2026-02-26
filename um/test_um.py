from um import count


def test_count_single_word() -> None:
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1


def test_count_with_punctuation() -> None:
    assert count("hello, um, world") == 1
    assert count("um? um! um.") == 3


def test_count_not_substring() -> None:
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_count_multiple_words() -> None:
    assert count("um um um") == 3
    assert count("Um, thanks... um") == 2

