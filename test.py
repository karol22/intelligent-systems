
# Karol Jose Gutierrez Suarez A01024536
#
# Rafael Elu Huacuja A01634309
#
# Jorge Andrés Pietra Santa Ochoa A00226522

import numpy as np


NUM_KIDS = 16
NUM_CHOCOLATES = 8
FRIENDS_BY_KID = [[5, 6, 15],
                 [2, 3, 7],
                 [1, 3, 4],
                 [1, 2, 4, 7],
                 [2, 3],
                 [0, 6, 15],
                 [0, 5, 15],
                 [1, 3, 8, 9, 13, 14],
                 [7, 9, 13, 14],
                 [7, 8, 13, 14],
                 [11, 12],
                 [10, 12],
                 [10, 11],
                 [7, 8, 9, 14],
                 [7, 8, 9, 13],
                 [0, 5, 6]]

state = [1] * NUM_CHOCOLATES + [0] *(NUM_KIDS - NUM_CHOCOLATES)
np.random.shuffle(state)
print(state)

def cost(state):
    totalCost = 0
    for i in range(0, len(state)):
        if state[i] == 0:
            totalCost += 2 + len(FRIENDS_BY_KID[i])
    return totalCost


def possibleMoves(state):
    moves = []
    