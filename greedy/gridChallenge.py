# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
# Example
# grid = ['abc','ade','efg']
# The grid is illustrated below.
# a b c
# a d e
# e f g
# The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

# Function Description
# Complete the gridChallenge function in the editor below.
# gridChallenge has the following parameter(s):
# - string grid[n]: an array of strings

# Returns
# string: either YES or NO

# Input Format
# The first line contains t, the number of testcases.
# Each of the next t sets of lines are described as follows:
# - The first line contains n, the number of rows and columns in the grid.
# - The next n lines contains a string of length n

# Constraints
# 1 ≤ t ≤ 100
# 1 ≤ n ≤ 100
# Each string consists of lowercase letters in the range ascii[a-z]

# Output Format
# For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.

# Sample Input
#     STDIN   Function
#     ----- --------
#     1       t = 1
#     5       n = 5
#     ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
#     fghij
#     olmkn
#     trpqs
#     xywuv

# Sample Output
#     YES

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid: list) -> str:
    # Write your code here
    for i in range(n):
        grid[i] = sorted(grid[i])

    for i in range(len(grid[0])):
        for j in range(1, len(grid[0])):
            if(grid[j-1][i] > grid[j][i]):
                return 'NO'
                
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
