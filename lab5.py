import random

import genetic_algorithm
import genetic_util
from params import FuzzyInputVariable_3Trapezoids, FuzzyInputVariable_2Trapezoids, FuzzyInputVariable_List_Trapezoids, \
    FuzzyInputVariable_2Sigmoids
from operators import productN

import numpy as np
# from helps_and_enhancers import *
import matplotlib
import matplotlib.pyplot as plt
from ANFIS import ANFIS
import time
import copy
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


def test_genetic_algorithm():
    x = genetic_util.generate_population()

    x, y = genetic_algorithm.run_genetic_algorithm(x, genetic_util.fun1, 200, genetic_algorithm.roulette_square,
                                                   0.8,
                                                   2, 0.1, 2, 8)
    pass


def test_genetic_algorithm2():
    x = genetic_util.generate_population2()

    x, y = genetic_algorithm.run_genetic_algorithm(x, genetic_util.fun2, 1000, genetic_algorithm.roulette_square,
                                                   0.8,
                                                   2, 0.1, 2, 8, minimizing=True)
    pass


# test_genetic_algorithm()
# test_genetic_algorithm2()
pass


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


def generate_initial_population(population_number: int):
    population = [[round(random.uniform(0.0, 1.0), 5) for i in range(46)] for j in range(population_number)]
    # population.append(get_anfis_initial_parameters_from_previous_exc())
    return population


def get_anfis_initial_parameters_from_previous_exc():
    var_list, data, labels = generate_anfis_data()
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=25)

    # x1 = [item for sublist in premises for item in sublist]
    # x1 = np.array(x1).flatten()
    # x2 = op
    # x3 = tsk.flatten()

    fis = ANFIS(var_list, X_train.T, y_train)
    x0 = fis.get_merged_anfis_parameters()

    return x0


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


x, y = genetic_algorithm.run_genetic_algorithm(generate_initial_population(1000), anfis_fitness_function, 1000,
                                               genetic_algorithm.roulette_square,
                                               0.8,
                                               2, 0.1, 2, 8, minimizing=True)
print("x = ", x, "y = ", y)
print("max: x = ", x[y.index(min(y))], ", y = ", min(y))

show_results_for_gives_x(x[y.index(max(y))])

# x = [0.95, 0.02, 0.13, 0.99, 0.0, 0.98, 0.92, 0.76, 0.46, 0.09, 0.86, 0.38, 0.79, 0.8, 0.96, 1.0, 0.92, 0.94, 0.98,
#      0.95, 0.97, 0.88, 0.99, 0.06, 0.97, 1.0, 1.0, 0.01, 1.0, 0.98, 1.0, 0.95, 0.99, 1.0, 0.99, 0.99, 0.97, 1.0, 1.0,
#      1.0, 1.0, 0.98, 1.0, 0.99, 0.99, 0.99]
# print("y = ", anfis_fitness_function(x))
# show_results_for_gives_x(x)

pass
