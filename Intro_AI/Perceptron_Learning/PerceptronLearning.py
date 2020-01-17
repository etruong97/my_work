# Evan Truong

import numpy as np
import random

# input: pos_points -> a list containing tuples of integers
#        neg_points -> a list containing tuples of integers
# output: a weight vector that classifies the positive and negative points
def perceptron_learning(pos_points, neg_points):
    # randomly generate a weight of equal dimension as points
    weight = []
    for i in range(len(pos_points[0])):
        r = random.randint(0, 10)
        weight.append(r)
    weight = tuple(weight)

    # extend vector for each point in pos_points
    for p in range(len(pos_points)):
        ls = list(pos_points[p])
        ls.insert(0, 1)
        pos_points[p] = tuple(ls)

    # extend vector for each point in neg_points
    for p in range(len(neg_points)):
        ls = list(neg_points[p])
        ls.insert(0, 1)
        neg_points[p] = tuple(ls)

    # counter to keep track of successful checks
    counter = 0
    while True:
        for point in pos_points:
            # dot product between weight and point
            product = np.dot(weight, point)
            # adds weight and point vectors if product <= 0
            if product <= 0:
                counter = 0
                weight = np.add(weight, point)
            else:
                counter += 1

        for point in neg_points:
            # dot product between weight and point
            product = np.dot(weight, point)
            # adds weight and point vectors if product > 0
            if product > 0:
                counter = 0
                weight = np.subtract(weight, point)
            else:
                counter += 1

        # returns the weight if all points pass the checks from above
        if counter >= len(pos_points) + len(neg_points):
            break

    return weight


if __name__ == '__main__':
    p = [(1, 1)]
    n = [(0, 1), (0, 0), (1, 0)]
    print(perceptron_learning((0, 0), p, n))
