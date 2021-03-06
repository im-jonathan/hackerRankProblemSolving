# Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?
# Consider an array of n distinct integers, arr = [a[0], a[1],...,a[n-1]]. George can swap any two elements of the array any number of times. An array is beautiful if the sum of |arr[i]-arr[i-1]| among 0 < i < n is minimal.
# Given the array arr, determine and return the minimum number of swaps that should be performed in order to make the array beautiful.
# Example
# arr = [7, 15, 12, 3]
# One minimal array is [3, 7, 12, 15]. To get there, George performed the following swaps:
#     Swap      Result
#     [7, 15, 12, 3]
#     3 7   [3, 15, 12, 7]
#     7 15  [3, 7, 12, 15]
# It took 2 swaps to make the array beautiful. This is minimal among the choices of beautiful arrays possible.

# Function Description
# Complete the lilysHomework function in the editor below.
# lilysHomework has the following parameter(s):
# - int arr[n]: an integer array

# Returns
# - int: the minimum number of swaps required

# Input Format
# The first line contains a single integer,n , the number of elements in arr.
# The second line contains n space-separated integers, arr[i].

# Constraints
# 1 ≤ n ≤ 10^5
# 1 ≤ arr[i] ≤ 2x10^9

# Sample Input
#     STDIN       Function
#     ----- --------
#     4           arr[]size n = 4
#     2 5 3 1     arr = [2, 5, 3, 1]

# Sample Output
#     2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def get_swaps(dict_arr: dict, sort_arr: list, rev: bool=False) -> int:
    swaps = {}
    for i, a in enumerate(sort_arr[::not rev or -1]):
        b = dict_arr[a]
        while True:
            try:
                b = swaps[b]
            except KeyError:
                break
        if b != i:
            swaps[i] = b

    return len(swaps)


def lilysHomework(arr: list) -> int:
    # Write your code here
    sort_arr = sorted(arr)
    dict_arr = {a: i for i, a in enumerate(arr)}
    return min(get_swaps(dict_arr, sort_arr), get_swaps(dict_arr, sort_arr, rev=True))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
