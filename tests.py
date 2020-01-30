from random import randrange

from genetic_util import int_to_binary_string


def crossover_test():
    x1 = "10000110"
    x2 = "01110110"
    word_length = len(x1)
    num_of_points_to_cross = 4
    positions = []
    # for i in range(0, num_of_points_to_cross):
    #     point = randrange(word_length)
    #     while point in positions:
    #         point = randrange(word_length)
    #     positions.append(point)
    positions = [5, 2]
    positions.sort()
    print("Positions: ", positions)
    nx1 = ""
    nx2 = ""
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
    print("Before crossing: ", x1, ", ", x2)
    print("After crossing: ", nx1, ", ", nx2)

crossover_test()