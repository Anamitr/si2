from random import randrange
import random

import numpy as np
from sklearn.model_selection import train_test_split

from ANFIS import ANFIS
from params import FuzzyInputVariable_2Sigmoids


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


def generate_initial_population_for_anfis(population_number: int):
    population = [[round(random.uniform(0.0, 1.0), 5) for i in range(46)] for j in range(population_number)]
    # population.append(get_anfis_initial_parameters_from_previous_exc())
    return population


def anfis_fitness_function(x: list):
    var_list, data, labels = generate_anfis_data()
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=25)

    fis = ANFIS(var_list, X_train.T, y_train)
    return fis.get_absolute_error(x)


def show_results_for_gives_x(x: list):
    var_list, data, labels = generate_anfis_data()
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=25)

    fis = ANFIS(var_list, X_train.T, y_train)

    fis.show_results_in_4d_for_given_x(x)


def generate_anfis_data():
    x = np.arange(0.1, 10, 0.5)
    # y = np.arange(0, 10, 0.1)
    # z = np.arange(0, 10, 0.1)
    x, y, z = np.meshgrid(x, x, x)

    dataX = x.flatten()
    dataY = y.flatten()
    dataZ = z.flatten()
    dataXYZ = np.column_stack((dataX, dataY, dataZ))

    output = (dataX ** 0.5 + dataY ** (-1) + dataZ ** 1.5) ** 2

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(dataX, dataY, dataZ, c=output, cmap=plt.hot())
    # fig.canvas.set_window_title('data')
    # plt.show()

    pass

    # varX = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "XAxis", ["L", "H"])
    # varY = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "YAxis", ["L", "H"])
    # varZ = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "ZAxis", ["L", "H"])
    #
    # varX.show()

    varX = FuzzyInputVariable_2Sigmoids("XAxis", ["L", "H"], 0.5, 0.5)
    varY = FuzzyInputVariable_2Sigmoids("XAxis", ["L", "H"], 0.5, 0.5)
    varZ = FuzzyInputVariable_2Sigmoids("XAxis", ["L", "H"], 0.5, 0.5)

    # varX.show()

    return [varX, varY, varZ], dataXYZ, output