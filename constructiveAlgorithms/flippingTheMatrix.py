# Sean invented a game involving a 2nx2n matrix where each cell of the matrix contains an integer.
# He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the nxn submatrix located in the upper-left quadrant of the matrix.
# Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.
# Example
# matrix = [[1,2],[3,4]]
#     1 2
#     3 4
# It is 2x2 and we want to maximize the top left quadrant, a 1x1 matrix. Reverse row 1:
#     1 2
#     4 3
# And now reverse column 0:
#     4 2
#     1 3
# The maximal sum is 4.

# Function Description
# Complete the flippingMatrix function in the editor below.
# flippingMatrix has the following parameters:
# - int matrix[2n][2n]: a 2-dimensional array of integers

# Returns
# - int: the maximum sum possible.

# Input Format
# The first line contains an integer q, the number of queries.
# The next q sets of lines are in the following format:
# - The first line of each query contains an integer, n.
# - Each of the next 2n lines contains 2n space-separated integers matrix[i][j] in row i of the matrix.

# Constraints
# 1 ≤ q ≤ 16
# 1 ≤ n ≤ 128
# 0 ≤ matrix[i][j] ≤ 4096, where 0 ≤ i,j < 2n.

# Sample Input
#     STDIN           Function
#     ----- --------
#     1               q = 1
#     2               n = 2
#     112 42 83 119   matrix = [[112, 42, 83, 119], [56, 125, 56, 49],
#     56 125 56 49              [15, 78, 101, 43], [62, 98, 114, 108]]
#     15 78 101 43
#     62 98 114 108

# Sample Output
#     414

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix: list) -> int:
    # Write your code here
    result = 0
    len_matrix = len(matrix)
    middle_idx = len_matrix - 1
    for i in range(len_matrix//2):
        for j in range(len_matrix//2):
            result += max(
                matrix[i][j],
                matrix[i][middle_idx-j],
                matrix[middle_idx-i][j],
                matrix[middle_idx-i][middle_idx-j]
            )
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
