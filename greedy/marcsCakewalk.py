# Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. If Marc has eaten j cupcakes so far, after eating a cupcake with calories he must walk at least 2^j x c miles to maintain his weight.
# Example
# calories = [5,10,7]
# If he eats the cupcakes in the order shown, the miles he will need to walk are (2^0 x5)+(2^1 x10)+(2^2 x7)=5+20+28=53. This is not the minimum, though, so we need to test other orders of consumption. In this case, our minimum miles is calculated as (2^0 x10)+(2^1 x7)+(2^2 x5)=10+14+20=44.
# Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.

# Function Description
# Complete the marcsCakewalk function in the editor below.
# marcsCakewalk has the following parameter(s):
# - int calorie[n]: the calorie counts for each cupcake

# Returns
# long: the minimum miles necessary

# Input Format
# The first line contains an integer n, the number of cupcakes in calories.
# The second line contains n space-separated integers, calories[i].

# Constraints
# 1 ≤ n ≤ 40
# 1 ≤ c[i] ≤ 1000

# Sample Input 0
#     3
#     1 3 2

# Sample Output 0
#     11

# Sample Input 1
#     4
#     7 4 9 6

# Sample Output 1
#     79

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#


def marcsCakewalk(calorie: list) -> int:
    # Write your code here
    calorie = sorted(calorie, reverse=True)
    data = [calorie[i]*(2**i) for i in range(len(calorie))]
    return sum(data)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
