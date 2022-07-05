from vowel_count import kata


def test_vowel_count():
    assert kata.count_vowels('aerial') == 4


def test_vowel_count_with_comprehension():
    assert kata.count_vowels_with_comprehension('aerial') == 4
