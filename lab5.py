import genetic_algorithm


def test_genetic_algorithm():
    x = genetic_algorithm.generate_population()

    x, y = genetic_algorithm.run_genetic_algorithm(x, genetic_algorithm.fun1, 200, genetic_algorithm.roulette_square,
                                                   0.8,
                                                   2, 0.1, 2, 8)
    pass


pass
