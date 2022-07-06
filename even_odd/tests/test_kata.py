from even_odd import kata


def test_is_even():
    assert kata.is_even_or_odd(2) == 'Even'


def test_is_odd():
    assert kata.is_even_or_odd(1) == 'Odd'
