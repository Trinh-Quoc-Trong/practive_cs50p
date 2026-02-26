from bank import value


def test_hello_case_insensitive() -> None:
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HeLlO") == 0


def test_hello_phrases() -> None:
    assert value("hello world") == 0
    assert value("Hello friend") == 0


def test_start_with_h() -> None:
    assert value("hi") == 20
    assert value("how are you") == 20
    assert value("Hola") == 20
    assert value("h") == 20


def test_no_h_start() -> None:
    assert value("good afternoon") == 100
    assert value("what's happening") == 100
    assert value("Sup") == 100


def test_empty() -> None:
    assert value("") == 100
