# Goodland is a country with a number of evenly spaced cities along a line. The distance between adjacent cities is 1 unit. There is an energy infrastructure project planning meeting, and the government needs to know the fewest number of power plants needed to provide electricity to the entire list of cities. Determine that number. If it cannot be done, return -1.
# You are given a list of city data. Cities that may contain a power plant have been labeled 1. Others not suitable for building a plant are labeled 0. Given a distribution range of k, find the lowest number of plants that must be built such that all cities are served. The distribution range limits supply to cities where distance is less than k.
# Example
# k = 3
# arr = [0,1,1,1,0,0,0]
# Each city is 1 unit distance from its neighbors, and we'll use 0 based indexing. We see there are 3 cities suitable for power plants, cities 1, 2 and 3. If we build a power plant at arr[2], it can serve arr[0] through arr[4] because those endpoints are at a distance of 2 and 2<k. To serve arr[6], we would need to be able to build a plant in city 4, 5 or 6. Since none of those is suitable, we must return -1. It cannot be done using the current distribution constraint.

# Function Description
# Complete the pylons function in the editor below.
# pylons has the following parameter(s):
# - int k: the distribution range
# - int arr[n]: each city's suitability as a building site

# Returns
# int: the minimum number of plants required or -1

# Input Format
# The first line contains two space-separated integers n and k, the number of cities in Goodland and the plants' range constant.
# The second line contains n space-separated binary integers where each integer indicates suitability for building a plant.

# Constraints
# 1 ≤ k ≤ n ≤ 10^5
# Each arr[i] ∈ {0,1}.
# Subtask
# 1 ≤ k ≤ n ≤ 1000 for 40% of the maximum score.

# Output Format
# Print a single integer denoting the minimum number of plants that must be built so that all of Goodland's cities have electricity. If this is not possible for the given value of k, print -1.

# Sample Input
#     STDIN         Function
#     ----- --------
#     6 2           arr[] size n = 6, k = 2
#     0 1 1 1 1 0   arr = [0, 1, 1, 1, 1, 0]

# Sample Output
#     2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pylons(k: int, arr: list) -> int:
    # Write your code here
    n = len(arr)
    start = 0
    last_pylon = -1

    total_pylons = 0
    while(start < n):
        furthest = min(start+k-1, n-1)

        for i in range(furthest, last_pylon, -1):
            if arr[i]:
                total_pylons += 1
                start = i+k
                last_pylon = i
                break
        else:
            return -1

    return total_pylons


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
