from square_digits import kata


def test_square_every_digit():
    assert kata.square_every_digit(9119) == 811181
    assert kata.square_every_digit(0) == 0
    assert kata.square_every_digit(1) == 1


def test_square_every_digit_with_comprehension():
    assert kata.square_every_digit_with_comprehension(9119) == 811181
    assert kata.square_every_digit(0) == 0
    assert kata.square_every_digit(1) == 1
