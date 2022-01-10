# Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.
# Example
# arr = [5,6,8,11]
# 8 is between two subarrays that sum to 11.
# arr = [1]
# The answer is [1] since left and right sum to 0.
# You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is , return YES. Otherwise, return NO.

# Function Description
# Complete the balancedSums function in the editor below.
# balancedSums has the following parameter(s):
# - int arr[n]: an array of integers

# Returns
# string: either YES or NO

# Input Format
# The first line contains T, the number of test cases.
# The next T pairs of lines each represent a test case.
# - The first line contains n, the number of elements in the array arr.
# - The second line contains n space-separated integers arr[i] where 0 ≤ i < n.

# Constraints
# 1 ≤ T ≤ 10
# 1 ≤ n ≤ 10^5
# 1 ≤ arr[i] ≤ 2x10^4
# 0 ≤ i < n

# Sample Input 0
#     2
#     3
#     1 2 3
#     4
#     1 2 3 3

# Sample Output 0
#     NO
#     YES
    
# Sample Input 1
#     3
#     5
#     1 1 4 1 1
#     4
#     2 0 0 0
#     4
#     0 0 2 0
# Sample Output 1
#     YES
#     YES
#     YES


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr: list) -> str:
    # Write your code here
    difference = 0
    left_index = 0
    compare_count = n - 1
    for i in range(n+1):
        if difference > 0:
            difference -= arr[compare_count + left_index - i]
        else:
            difference += arr[left_index]
            left_index += 1
    data = ['NO', 'YES'][difference == 0]
    return data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
