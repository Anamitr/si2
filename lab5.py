import genetic_algorithm
import genetic_util
from genetic_util import generate_anfis_data

# from helps_and_enhancers import *
from ANFIS import ANFIS
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


x, y = genetic_algorithm.run_genetic_algorithm(genetic_util.generate_initial_population_for_anfis(1000),
                                               genetic_util.anfis_fitness_function, 1000,
                                               genetic_algorithm.roulette_square,
                                               0.8,
                                               2, 0.1, 2, minimizing=True)
print("x = ", x, "y = ", y)
print("max: x = ", x[y.index(min(y))], ", y = ", min(y))

genetic_util.show_results_for_gives_x(x[y.index(max(y))])

# x = [0.95, 0.02, 0.13, 0.99, 0.0, 0.98, 0.92, 0.76, 0.46, 0.09, 0.86, 0.38, 0.79, 0.8, 0.96, 1.0, 0.92, 0.94, 0.98,
#      0.95, 0.97, 0.88, 0.99, 0.06, 0.97, 1.0, 1.0, 0.01, 1.0, 0.98, 1.0, 0.95, 0.99, 1.0, 0.99, 0.99, 0.97, 1.0, 1.0,
#      1.0, 1.0, 0.98, 1.0, 0.99, 0.99, 0.99]
# print("y = ", anfis_fitness_function(x))
# show_results_for_gives_x(x)

pass
