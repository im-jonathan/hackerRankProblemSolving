# You are given an unordered array of unique integers incrementing from 1. You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.
# Example
# arr = [1,2,3,4]
# k = 1
# The following arrays can be formed by swapping the 1 with the other elements:
# [2, 1, 3, 4]
# [3, 2, 1, 4]
# [4, 2, 3, 1]
# The highest value of the four(including the original) is [4,2,3,1]. If k≥2, we can swap to the highest possible value: [4,2,3,1].

# Function Description
# Complete the largestPermutation function in the editor below. It must return an array that represents the highest value permutation that can be formed.
# largestPermutation has the following parameter(s):
# - int k: the maximum number of swaps
# - int arr[n]: an array of integers

# Input Format
# The first line contains two space-separated integers n and k, the length of arr and the maximum swaps that can be performed. The second line contains n distinct space-separated integers from 1 to n as arr[i] where 1 ≤ arr[i] ≤ n.

# Constraints
# 1 ≤ n ≤ 10^5
# 1 ≤ k ≤ 10^9

# Output Format
# Print the lexicographically largest permutation you can make with at most k swaps.

# Sample Input 0
#     STDIN       Function
#     ----- --------
#     5 1         n = 5, k = 1
#     4 2 3 5 1   arr = [4, 2, 3, 5, 1]

# Sample Output 0
#     5 2 3 4 1

# Sample Input 1
#     3 1
#     2 1 3

# Sample Output 1
#     3 1 2
    
# Sample Input 2
#     2 1
#     2 1

# Sample Output 2
#     2 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def largestPermutation(k: int, arr: list) -> list:
    # Write your code here
    n = len(arr)
    d = {}
    i = 0
    while i < n:
        d[arr[i]] = i
        i += 1
    i = 0
    while n > 0 and k > 0:
        if arr[i] < n:
            tmp = d[n]
            arr[d[n]] = arr[i]
            arr[i] = n
            tmp = d[arr[d[n]]]
            d[arr[d[n]]] = d[n]
            d[n] = tmp
            k -= 1
        n -= 1
        i += 1
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
