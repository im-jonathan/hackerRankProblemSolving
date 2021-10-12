#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def queensAttack(n: int, k: int, r_q: int, c_q: int, obstacles: list) -> int:
    # Write your code here
    obstacles = {(ob[0], ob[1]) for ob in obstacles}
    movements = [(1, 0), (0, 1), (-1, 0), (0, -1),
                 (1, 1), (-1, -1), (-1, 1), (1, -1)]
    count = 0

    for move in movements:
        cr, cc = r_q, c_q
        while (cr + move[0] >= 1 and cr + move[0] <= n) and (cc + move[1] >= 1 and cc + move[1] <= n):
            cr += move[0]
            cc += move[1]
            if (cr, cc) in obstacles:
                break
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
