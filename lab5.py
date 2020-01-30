import genetic_algorithm
import genetic_util


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
test_genetic_algorithm2()
pass
