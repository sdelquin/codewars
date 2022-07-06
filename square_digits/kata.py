# https://www.codewars.com/kata/546e2562b03326a88e000020


def square_every_digit(number: int) -> int:
    output = []
    for digit in str(number):
        output.append(str(int(digit) ** 2))
    return int(''.join(output))


def square_every_digit_with_comprehension(number: int) -> int:
    return int(''.join(str(int(d) ** 2) for d in str(number)))
