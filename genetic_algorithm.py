# krzyżowanie jednopunktowe
# koło ruletki liniowe, kwadratowe i logarytmiczne

# prawd. krzyzowania = 0.8
# ilosc punktow w ktorych zachodzi krzyzowanie
# prawd. mutacji
# ilosc miejsc w ktorych zachodzi mutacja
# ile generacji
# wielkosc genotypu
# wybor metody selekcji

# zewnetrznie podawana funkcja przystosowania

import random
from random import randrange
import math

import genetic_util
from genetic_util import int_to_binary_string, generate_population, fun1
from genetic_util import binary_string_to_int


def turn_around_for_minimizing(y):
    y_max = max(y)
    minimized_y = [y_max - item for item in y]
    return minimized_y


def roulette_linear(x: list, y: list):
    y_sum = 0
    for item in y:
        y_sum = y_sum + item
    print("y_sum = ", y_sum)

    drawn_numbers = []
    for i in range(0, len(y)):
        drawn_numbers.append(random.uniform(0, y_sum))
        # drawn_number = randrange(y_sum)
    print("Drawn numbers: ", drawn_numbers)

    drawn_specimens = []
    for i in range(0, len(y)):
        drawn_number = drawn_numbers[i]
        roulette_sum = 0
        for j in range(0, len(y)):
            roulette_sum = roulette_sum + y[j]
            if roulette_sum >= drawn_number:
                drawn_specimens.append(x[j])
                break

    print("Drawn specimens: ", drawn_specimens)
    return drawn_specimens


def roulette_square(x: list, y: list):
    y_squared = [item ** 2 for item in y]
    return roulette_linear(x, y_squared)


def roulette_logarithmic(x: list, y: list):
    y_logarithmic = [math.log(item, LOGARITHM_BASE) for item in y]
    return roulette_linear(x, y_logarithmic)


def crossover(x: list, cross_prob: float, num_of_points_to_cross: int):
    num_of_potential_crossovers = int(len(x) / 2)
    # x_string = [int_to_binary_string(item, word_length) for item in x]
    x_string = x
    new_population = []
    word_length = len(x_string)

    for i in range(0, num_of_potential_crossovers):
        positions = []
        x1 = x_string[i * 2]
        x2 = x_string[i * 2 + 1]
        if (randrange(100) / 100) <= cross_prob:
            for i in range(0, num_of_points_to_cross):
                point = randrange(word_length)
                while point in positions:
                    point = randrange(word_length)
                positions.append(point)
            positions.sort()
            # print("Positions: ", positions)
            nx1 = []
            nx2 = []
            odd_flag = True
            if len(positions) == 1:
                nx1 = x2[:positions[0]] + x1[positions[0]:]
                nx2 = x1[:positions[0]] + x2[positions[0]:]
            else:
                for i in range(0, len(positions)):
                    if i == 0:
                        nx1 += x2[:positions[i]]
                        nx2 += x1[:positions[i]]
                        odd_flag = False
                    elif i == (len(positions) - 1):
                        if odd_flag:
                            nx1 += x2[positions[i - 1]:positions[i]]
                            nx2 += x1[positions[i - 1]:positions[i]]
                            nx1 += x1[positions[i]:]
                            nx2 += x2[positions[i]:]
                            odd_flag = False
                        else:

                            nx1 += x1[positions[i - 1]:positions[i]]
                            nx2 += x2[positions[i - 1]:positions[i]]
                            nx1 += x2[positions[i]:]
                            nx2 += x1[positions[i]:]
                            odd_flag = True
                    else:
                        if odd_flag:
                            nx1 += x2[positions[i - 1]:positions[i]]
                            nx2 += x1[positions[i - 1]:positions[i]]
                            odd_flag = False
                        else:
                            nx1 += x1[positions[i - 1]:positions[i]]
                            nx2 += x2[positions[i - 1]:positions[i]]
                            odd_flag = True
            # print("Before crossing: ", x1, ", ", x2)
            # print("After crossing: ", nx1, ", ", nx2)
            new_population.extend([nx1, nx2])
        else:
            new_population.extend([x[i * 2], x[i * 2 + 1]])
    return new_population


def mutate(population, mutation_probability, num_of_mutation_places):
    # x_string = [int_to_binary_string(item, word_length) for item in population]
    x_string = population
    new_population = []
    # print("Before mutations: ", x_string)
    for item in x_string:
        # print("Mutating item: ", item)
        if (randrange(100) / 100) <= mutation_probability:
            mutation_places = []
            for i in range(0, num_of_mutation_places):
                place = randrange(len(item))
                while place in mutation_places:
                    place = randrange(len(item))
                # print("Mutation place: ", place)
                item[place] = round(random.uniform(0.0, 1.0), 2)
        new_population.append(item)
    # print("After mutations: ", new_population)
    return new_population


FITNESS_FUNCTION = fun1
ROULETTE_FUNCTION = roulette_square
CROSS_PROBABILITY = 0.8
NUM_OF_POINTS_TO_CROSS = 2
MUTATION_PROBABILTY = 0.1
NUM_OF_MUTATION_PLACES = 2
NUM_OF_GENERATIONS = 200
GENOTYPE_SIZE = 8
SELECTION_METHOD = None

LOGARITHM_BASE = 10


# x = generate_population()
# print("Initial population:\n", x)
#
# y = [FITNESS_FUNCTION(item) for item in x]
# print("Initial fitness:\n", y)


# for i in range(0, NUM_OF_GENERATIONS):
#     drawn_specimens = ROULETTE_FUNCTION(x, y)
#
#     crossed_population = crossover(drawn_specimens, CROSS_PROBABILITY, NUM_OF_POINTS_TO_CROSS, GENOTYPE_SIZE)
#     # print("Population after crossover: ", crossed_population)
#
#     mutated_population = mutate(crossed_population, MUTATION_PROBABILTY, NUM_OF_MUTATION_PLACES, GENOTYPE_SIZE)
#     # print("Population after mutation: ", mutated_population)
#
#     x = mutated_population
#
#     y = [FITNESS_FUNCTION(item) for item in x]
#     print("Fitness in generation num ", i, ":\n", y)


def run_genetic_algorithm(population: list, fitness_function, num_of_generations, roulette_function, cross_probability,
                          num_of_points_to_cross, mutation_probabilty, num_of_mutation_places,
                          minimizing=True):
    x = population
    print("Initial population:\n", x)

    y = [round(fitness_function(item), 4) for item in x]

    print("Initial fitness:\n", y)
    global_max_y = max(y)
    global_max_x = x[y.index(max(y))]
    for i in range(0, num_of_generations):
        if minimizing:
            y = turn_around_for_minimizing(y)
        drawn_specimens = roulette_function(x, y)

        crossed_population = crossover(drawn_specimens, cross_probability, num_of_points_to_cross)
        # print("Population after crossover: ", crossed_population)

        mutated_population = mutate(crossed_population, mutation_probabilty, num_of_mutation_places)
        print("Population after mutation: ", mutated_population)

        x = mutated_population

        y = [round(fitness_function(item), 4) for item in x]
        print("Fitness in generation num ", i, ":\n", y)
        if minimizing:
            y_max = min(y)
        else:
            y_max = max(y)
        print("Generation", i, "best =", y_max)
        if y_max < global_max_y:
            global_max_y = y_max
            global_max_x = x[y.index(y_max)]

    print("Global best = ", y_max)

    return x, y


# x, y = run_genetic_algorithm(genetic_util.generate_initial_population_for_anfis(1000),
#                              genetic_util.anfis_fitness_function, 10,
#                              roulette_square,
#                              0.8,
#                              2, 0.1, 2, minimizing=True)
# print("x = ", x, "y = ", y)
# print("max: x = ", x[y.index(min(y))], ", y = ", min(y))
#
# genetic_util.show_results_for_gives_x(x[y.index(max(y))])
