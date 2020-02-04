# Algorytm roju cząstek

# Wybiermay najlepszą cząsteczke z roju
# Każdą pozycje zapamiętujemy jako najlepszą pozycję tej cząsteczki
# Nadajemy im prędkości i kierunek
# Iterujemy przez wszystkie cząsteczki i modyfikujemy prędkość biorąc pod uwagę trzy czynniki
# V = a1 * v + a2 * c + a3 * r
# c - mądrość samej cząsteczki
# r - mądrość roju
# a3 * r(R-x)
# r - liczba losowa [0; 1]
# x = x + V
# Nadpisujemy cząsteczkę jeśli osiągnęła lepszą pozycję i wartość najlepszej cząsteczki

# V = p1 * V + p2 * r1 (C - x) + p3 * r2 * (R - x)
# p2 - jak czasteczka ufa samej sobie
# r1 - liczba losowa
# p3 - jak ufam calemu rojowi

# 0.5, 2, 2
import random

import genetic_util


def calculate_velocity(x, p1, p2, p3, v0, c_max, r_max):
    r1 = round(random.uniform(0.0, 1.0), 5)
    r2 = round(random.uniform(0.0, 1.0), 5)
    return p1 * v0 + p2 * r1 * (c_max - x) + p3 * r2 * (r_max - x)
    pass


# x = genetic_util.generate_population2()
# fitness_function = genetic_util.fun2
#
# y = [fitness_function(item) for item in x]
# y_best = y.copy()
#
# global_best_y = max(y)
# global_best_x = x[y.index(max(y))]
#
# velocities = [round(random.uniform(0.0, 1.0), 5) for item in x]
# velocities = [calculate_velocity(item, P1, P2, P3, 0, ) for item in x]
#
# for j in range(NUM_OF_MOVES):
#     for i in range(len(x)):
#         new_x = x[i] + velocities[i]
#         new_y = fitness_function(new_x)
#         if new_y > y_best[i]:
#             x[i] = new_x
#             y_best[i] = new_y
#         if new_y > global_best_y:
#             global_best_x = new_x
#             global_best_y = new_y
#
# print("Global best x = ", global_best_x)
# print("Global best y = ", global_best_y)


def is_lesser(y1, y2):
    return y1 < y2


def is_bigger(y1, y2):
    return y1 > y2


def run_particle_swarm_algorithm(population, fitness_function, num_of_moves, p1, p2, p3, better_func):
    x = population
    y = [fitness_function(item) for item in x]
    y_best = y.copy()
    x_best = x.copy()
    global_best_y = max(y)
    global_best_x = x[y.index(max(y))]

    velocities = [[round(random.uniform(0.0, 1.0), 5) for j in range(len(x[0]))] for i in range(len(x))]

    for m in range(num_of_moves):
        for i in range(len(x)):
            velocity = [calculate_velocity(x[i][j], p1, p2, p3, velocities[i][j], x_best[i][j], global_best_x[j]) for j
                        in range(len(x[i]))]
            velocities[i] = velocity
            x[i] = [sum(item) for item in zip(x[i], velocity)]
            # x[i] = [item + velocity for item in x[i]]

        y = [fitness_function(item) for item in x]
        for i in range(len(x)):
            if better_func(y[i], y_best[i]):
                y_best[i] = y[i]
                x_best[i] = x[i]
                if better_func(y_best[i], global_best_y):
                    global_best_y = y_best[i]
                    global_best_x = x_best[i]
        print("Num ", m, ", global_best_y = ", global_best_y)
        print("global_best_x = ", global_best_x)
        print("Population: ", x)
        print("y = ", y)

    return x_best, y_best, global_best_x, global_best_y


P1 = 0.5  # waga dotychczasowej predkosci
P2 = 2  # jak czasteczka ufa samej sobie
P3 = 2  # jak ufa calemu rojowi
NUM_OF_MOVES = 100

# x_best, y_best, global_best_x, global_best_y = run_particle_swarm_algorithm(genetic_util.generate_population2(),
#                                                                             genetic_util.fun2, NUM_OF_MOVES, P1, P2, P3,
#                                                                             is_bigger)

x_best, y_best, global_best_x, global_best_y = run_particle_swarm_algorithm(
    genetic_util.generate_initial_population_for_anfis(1000),
    genetic_util.anfis_fitness_function, NUM_OF_MOVES, P1, P2, P3,
    is_lesser)

pass
