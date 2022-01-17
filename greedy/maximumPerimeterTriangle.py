# Given an array of stick lengths, use 3 of them to construct a non-degenerate triangle with the maximum possible perimeter. Return an array of the lengths of its sides as 3 integers in non-decreasing order.
# If there are several valid triangles having the maximum perimeter:
# 1. Choose the one with the longest maximum side.
# 2. If more than one has that maximum, choose from them the one with the longest minimum side.
# 3. If more than one has that maximum as well, print any one them.
# If no non-degenerate triangle exists, return [-1].
# Example
# sticks=[1,2,3,4,5,10]
# The triplet (1,2,3) will not form a triangle. Neither will (4,5,10) or (2,3,5), so the problem is reduced to (2,3,4) and (3,4,5). The longer perimeter is 3+4+5=12.

# Function Description
# Complete the maximumPerimeterTriangle function in the editor below.
# maximumPerimeterTriangle has the following parameter(s):
# - int sticks[n]: the lengths of sticks available

# Returns
# int[3] or int[1]: the side lengths of the chosen triangle in non-decreasing order or -1

# Input Format
# The first line contains single integer n, the size of array sticks.
# The second line contains n space-separated integers sticks[i], each a stick length.

# Constraints
# 3 ≤ n ≤ 50
# 1 ≤ stricks[i] ≤ 10^9

# Sample Input 0
#     5
#     1 1 1 3 3

# Sample Output 0
#     1 3 3

# Sample Input 1
#     3
#     1 2 3

# Sample Output 1
#     -1

# Sample Input 2
#     6
#     1 1 1 2 3 5

# Sample Output 2
#     1 1 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks: list) -> list:
    # Write your code here
    flag = False
    sticks.sort(reverse=True)
    # print(sticks)
    list1 = []
    for i in range(len(sticks)):
        if i+2 < len(sticks) and sticks[i+2]+sticks[i+1] > sticks[i]:
            flag = True
            list1.append(sticks[i+2])
            list1.append(sticks[i + 1])
            list1.append(sticks[i])
            break

    if flag == True:
        return list1

    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
