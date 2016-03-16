from util.functions import concat_strings


def test_addition():
    assert(1 + 1 == 2)


def test_multiplication():
    assert(1 * 3 == 3)


def test_concat_strings():
    assert(concat_strings("a", "b") == "ab")
