from spin_words import kata


def test_spin_words():
    assert kata.spin_words('Hey fellow warriors', 5) == 'Hey wollef sroirraw'
    assert kata.spin_words('This is a test', 5) == 'This is a test'
    assert kata.spin_words('This is another test', 5) == 'This is rehtona test'


def test_spin_words_with_comprehension():
    assert (
        kata.spin_words_with_comprehension('Hey fellow warriors', 5)
        == 'Hey wollef sroirraw'
    )
    assert kata.spin_words_with_comprehension('This is a test', 5) == 'This is a test'
    assert (
        kata.spin_words_with_comprehension('This is another test', 5)
        == 'This is rehtona test'
    )
