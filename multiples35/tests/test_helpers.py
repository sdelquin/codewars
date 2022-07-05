from multiples35 import helpers


def test_multiple_of_3():
    assert helpers.multiple_of_3(3) is True
    assert helpers.multiple_of_3(4) is False


def test_multiple_of_5():
    assert helpers.multiple_of_5(5) is True
    assert helpers.multiple_of_5(6) is False
