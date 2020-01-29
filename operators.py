import numpy as np
from t_norms import *


def t_norm(args, op):
    op = np.array(op)
    min_val = np.min(args, axis=0)
    max_val = np.max(args, axis=0)
    return op * min_val + (1-op) * max_val


def productN(args, op):
    # print("args[0]:", args[0])
    # print("args[1]:", args[1])
    return np.product(args, axis=0)


def zadeh(args, op):
    # print("args[0]:", args[0])
    # print("args[1]:", args[1])
    return np.minimum(args[0], args[1])


def algebraic(args, op):
    return np.multiply(args[0], args[1])


def lukasiewicz(args, op):
    return operator_element_wise(args, lukasiewicz_t)


def fodor(args, op):
    return operator_element_wise(args, fodor_t)


def drastic(args, op):
    return operator_element_wise(args, drastic_t)


def einstein(args, op):
    return operator_element_wise(args, einstein_t)


def operator_element_wise(args, t_norm):
    result = np.zeros(args[0].shape, dtype=float)
    for i in range(0, len(args[0])):
        for j in range(0, len(args[0][0])):
            result[i][j] = t_norm(args[0][i][j], args[1][i][j])
    return result
