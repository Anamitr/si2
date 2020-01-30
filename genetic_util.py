from random import randrange
import random


def int_to_binary_string(x: int, num_of_chars: int) -> str:
    return ("{0:b}".format(x)).rjust(num_of_chars, "0")


def binary_string_to_int(x: str) -> int:
    return int(x, 2)


def generate_population():
    x = []
    [x.append(randrange(100)) for i in range(0, 20)]
    return x
    # return [134, 118, 95, 60]


def fun1(x: int):
    return 10 * x ^ 2 + 2 * x + 4


def generate_population2():
    x = [[round(random.uniform(0.0, 1.0), 2) for i in range(10)] for j in range(10)]
    return x


def fun2(x: list):
    return sum(x)
