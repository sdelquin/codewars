# https://www.codewars.com/kata/514b92a657cdc65150000006

from .helpers import multiple_of_3, multiple_of_5


def get_sum_below(limit):
    multiples = []
    for value in range(limit):
        if multiple_of_3(value) or multiple_of_5(value):
            multiples.append(value)
    return sum(multiples)


def get_sum_below_with_comprehension(limit):
    return sum(v for v in range(limit) if multiple_of_3(v) and multiple_of_5(v))
