from disemvowel_trolls import kata


def test_remove_vowels():
    assert kata.remove_vowels('This website is for losers LOL!') == 'Ths wbst s fr lsrs LL!'


def test_remove_vowels_with_comprehension():
    assert (
        kata.remove_vowels_with_comprehension('This website is for losers LOL!')
        == 'Ths wbst s fr lsrs LL!'
    )
