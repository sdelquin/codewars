from functools import partial


def multiple_of(value, factor):
    return value % factor == 0


multiple_of_3 = partial(multiple_of, factor=3)
multiple_of_5 = partial(multiple_of, factor=5)
