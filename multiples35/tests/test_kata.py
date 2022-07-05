from multiples35 import kata


def test_sum_below():
    assert kata.get_sum_below(10) == 23


def test_sum_below_negative():
    assert kata.get_sum_below(-1) == 0


def test_sum_below_with_comprehension():
    assert kata.get_sum_below(10) == 23


def test_sum_below_negative_with_comprehension():
    assert kata.get_sum_below(-1) == 0
