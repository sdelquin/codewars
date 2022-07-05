from vowel_count import helpers


def test_is_vowel():
    assert helpers.is_vowel('a') is True
    assert helpers.is_vowel('b') is False
