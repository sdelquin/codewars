from .helpers import is_vowel


def count_vowels(string):
    num_vowels = 0
    for char in string:
        if is_vowel(char):
            num_vowels += 1
    return num_vowels


def count_vowels_with_comprehension(string):
    return sum(is_vowel(c) for c in string)
