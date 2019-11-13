from params import FuzzyInputVariable_3Trapezoids, FuzzyInputVariable_2Trapezoids, FuzzyInputVariable_List_Trapezoids
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


# matplotlib.use('Qt5Agg')

def get_list_of_trapezoids(num_of_trapezoids: int):
    mf = [[1, 0, 0, 1]]
    for i in range(2, num_of_trapezoids):
        mf.append([i, 0, 1, 1])
    mf.append([num_of_trapezoids, 0, 1, 0])
    return mf


print("Multiplication table")

MULTIPLICATION_TABLE_SIZE = 3
NUM_OF_POINTS_IN_ONE_DIM = 10
MAX_TABLE_SIZE = 10

calculation_times = []

for i in range(10, MAX_TABLE_SIZE + 1):
    MULTIPLICATION_TABLE_SIZE = i
    print("MULTIPLICATION_TABLE_SIZE =", MULTIPLICATION_TABLE_SIZE)

    # Przygotowanie zbioru danych: XOR

    x = np.arange(1, MULTIPLICATION_TABLE_SIZE, (MULTIPLICATION_TABLE_SIZE - 1) / NUM_OF_POINTS_IN_ONE_DIM)
    x, y = np.meshgrid(x, x)

    dataX = x.flatten()
    dataY = y.flatten()
    dataXY1 = np.column_stack((dataX, dataY, np.ones(len(dataX))))
    dataXY = np.column_stack((dataX, dataY))

    # data_labels = np.logical_xor(dataX >= 0.5, dataY >= 0.5)
    dataXround = [int(round(x)) for x in dataX]
    dataYround = [int(round(y)) for y in dataY]
    data_labels = np.multiply(dataXround, dataYround)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    rgb = [[1, 0, 0] if cc else [0, 1, 0] for cc in data_labels]

    ax.scatter(dataX, dataY, data_labels, c=rgb)

    plt.show()

    # Utworzenie funkcji przynależności

    varX = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "XAxis", ["L", "H"])  # low, high
    varY = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "YAxis", ["L", "H"])

    # [1, 1.5] [1, 2] [1.5, 2]
    # mf1 = [[-0.5, 0.25, 0.25, 0.25], [0.5, 0.25, 0.1, 0.1]]
    #
    # # mf1 = [[1, 1, 1, 2], [1, 2, 2, 2]]
    # # mf1 = [[-0.5, 0.25, 0.5, 0.5]]
    #
    # mf2 = [[1, 0, 0, 1], [2, 0, 1, 0]]
    # mf3 = [[1, 0, 0, 1], [2, 0, 1, 1], [3, 0, 1, 0]]
    # mf4 = [[1, 0, 0, 1], [2, 0, 1, 1], [3, 0, 1, 1], [4, 0, 1, 0]]

    mf = get_list_of_trapezoids(MULTIPLICATION_TABLE_SIZE)
    varX = FuzzyInputVariable_List_Trapezoids(mf, "XAxis", ["L", "H"])
    varY = FuzzyInputVariable_List_Trapezoids(mf, "YAxis", ["L", "H"])

    # Wyświetlanie funkcji przynależnosci
    plt.figure()
    varX.show(np.arange(0, MULTIPLICATION_TABLE_SIZE + 1, 0.1))
    plt.legend()
    # plt.xlim(0, 3)

    # plt.figure()
    # varY.show(np.arange(0, 4, 0.1))
    # plt.legend()
    # # plt.xlim(0, 3)
    #
    # plt.show()

    X_train, X_test, y_train, y_test = train_test_split(dataXY, data_labels, test_size=0.2, random_state=25)

    fis = ANFIS([varX, varY], X_train.T, y_train)

    print("Parametry początkowe:\nPrzesłanki: ", fis.premises, "\nKonkluzje: ", fis.tsk)

    fis.show_results()

    start = time.time()
    fis.train(True, True, False, True, n_iter=100)
    end = time.time()
    print("TIME elapsed: ", end - start)
    calculation_times.append(end - start)
    fis.training_data = X_train.T
    fis.expected_labels = y_train
    fis.show_results()

    print("Konkluzje:", fis.tsk)

    fis.training_data = X_test.T
    fis.expected_labels = y_test
    fis.show_results()

    y_pred = fis.anfis_estimate_labels(fis.premises, fis.op, fis.tsk)
    y_pred = list(map(round, y_pred.flatten()))
    print(confusion_matrix(y_test, y_pred))

print("Calculation times:")
print(calculation_times)

x = list(range(2, MAX_TABLE_SIZE + 1))
plt.plot(x, calculation_times)
plt.show()
