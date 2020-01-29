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

matplotlib.use('Qt5Agg')

def run_anfis(var_list: list, data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=25)

    fis = ANFIS(var_list, X_train.T, y_train)

    fis.train(False, True, True, True, n_iter=50)

    fis.show_results_in_4d()
    fis.show_abs_error_results(y_train)
    fis.show_relative_error_results(y_train)


x = np.arange(0.1, 10, 0.5)
# y = np.arange(0, 10, 0.1)
# z = np.arange(0, 10, 0.1)
x, y, z = np.meshgrid(x, x, x)

dataX = x.flatten()
dataY = y.flatten()
dataZ = z.flatten()
dataXYZ = np.column_stack((dataX, dataY, dataZ))

output = (dataX ** 0.5 + dataY ** (-1) + dataZ ** 1.5) ** 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dataX, dataY, dataZ, c=output, cmap=plt.hot())

plt.show()

pass

# varX = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "XAxis", ["L", "H"])
# varY = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "YAxis", ["L", "H"])
# varZ = FuzzyInputVariable_2Trapezoids(0.5, 0.5, "ZAxis", ["L", "H"])
#
# varX.show()
# run_anfis([varX, varY, varZ], dataXYZ, output)

varX = FuzzyInputVariable_2Sigmoids("XAxis", ["L", "H"], 0.5, 0.5)
varY = FuzzyInputVariable_2Sigmoids("XAxis", ["L", "H"], 0.5, 0.5)
varZ = FuzzyInputVariable_2Sigmoids("XAxis", ["L", "H"], 0.5, 0.5)

varX.show()
run_anfis([varX, varY, varZ], dataXYZ, output)

# varY.show()
# [var.show() for var in [varX, varY, varZ]]
