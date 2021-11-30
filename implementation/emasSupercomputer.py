# Ema built a quantum computer! Help her test its capabilities by solving the problem below.
# Given a grid of size nxm, each cell in the grid is either good or bad.
# A valid plus is defined here as the crossing of two segments(horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.
# Find the two largest valid pluses that can be drawn on good cells in the grid, and return an integer denoting the maximum product of their areas. In the above diagrams, our largest pluses have areas of 5 and 9. The product of their areas is 5X9=45.
# Note: The two pluses cannot overlap, and the product of their areas should be maximal.

# Function Description
# Complete the twoPluses function in the editor below. It should return an integer that represents the area of the two largest pluses.
# twoPluses has the following parameter(s):
# - grid: an array of strings where each string represents a row and each character of the string represents a column of that row

# Input Format
# The first line contains two space-separated integers, n and m.
# Each of the next n lines contains a string of m characters where each character is either G(good) or B(bad). These strings represent the rows of the grid. If the yth character in the xth line is G, then (x,y) is a good cell. Otherwise it's a bad cell.

# Constraints
# 2 ≤ n ≤ 15
# 2 ≤ m ≤ 15

# Output Format
# Find 2 pluses that can be drawn on good cells of the grid, and return an integer denoting the maximum product of their areas.

# Sample Input 0
#     5 6
#     GGGGGG
#     GBBBGB
#     GGGGGG
#     GGBBGB
#     GGGGGG

# Sample Output 0
#     5

# Sample Input 1
#     6 6
#     BGBBGB
#     GGGGGG
#     BGBBGB
#     GGGGGG
#     BGBBGB
#     BGBBGB

# Sample Output 1
#     25

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#


def twoPluses(grid: list) -> int:
    # Write your code here
    for i in range(len(grid)):
        grid[i] = list(grid[i])
        grid[i].append('o')
        grid[i].insert(0, 'o')
    grid.append(['o' for i in range(len(grid[0]))])
    grid.insert(0, ['o' for i in range(len(grid[0]))])
    res = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == 'G':
                currCord = []
                currCord.append((i, j))
                area = 1
                start = 1
                res.append([area, currCord.copy()])
                while ((grid[i-start][j] == 'G') & (grid[i+start][j] == 'G') & (grid[i][j-start] == 'G') & (grid[i][j+start] == 'G')):
                    currCord.append((i-start, j))
                    currCord.append((i+start, j))
                    currCord.append((i, j-start))
                    currCord.append((i, j+start))
                    area += 4
                    start += 1
                    res.append([area, currCord.copy()])
    result = 0
    for i in range(len(res)-1):
        for j in range(i+1, len(res)):
            if (len(set(res[i][1]).intersection(set(res[j][1]))) == 0) & (res[i][0]*res[j][0] > result):
                result = res[i][0]*res[j][0]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
