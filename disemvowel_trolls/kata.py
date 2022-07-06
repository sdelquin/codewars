# https://www.codewars.com/kata/52fba66badcd10859f00097e

from .helpers import is_vowel


def remove_vowels(msg):
    output = []
    for char in msg:
        if not is_vowel(char):
            output.append(char)
    return ''.join(output)


def remove_vowels_with_comprehension(msg):
    return ''.join(c for c in msg if not is_vowel(c))
