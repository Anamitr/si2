def int_to_binary_string(x: int, num_of_chars: int) -> str:
    return ("{0:b}".format(x)).rjust(num_of_chars, "0")


def binary_string_to_int(x: str) -> int:
    return int(x, 2)
