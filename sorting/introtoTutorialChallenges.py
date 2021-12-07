# Sample Challenge
# This is a simple challenge to get things started. Given a sorted array (arr) and a number (V), can you print the index location of V in the array?
# Example
# arr = [1,2,3]
# V = 3

# Return 2 for a zero-based index array.
# If you are going to use the provided code for I/O, this next section is for you.

# Function Description
# Complete the introTutorial function in the editor below. It must return an integer representing the zero-based index of .
# introTutorial has the following parameter(s):
# - int arr[n]: a sorted array of integers
# - int V: an integer to search for

# Returns
# int: the index of V in arr
# The next section describes the input format. You can often skip it, if you are using included methods or code stubs.

# Input Format
# The first line contains an integer, V, a value to search for.
# The next line contains an integer, n, the size of arr. The last line contains n space-separated integers, each a value of arr[i] where 0 ≤ i < n.
# The next section describes the constraints and ranges of the input. You should check this section to know the range of the input.

# Constraints
# 1 ≤ n ≤ 1000
# -1000 ≤ V ≤ 1000, V ∈ arr
# V will occur in arr exactly once.
# This "sample" shows the first input test case. It is often useful to go through the sample to understand a challenge.

# Sample Input 0
#     STDIN           Function
#     -----           --------
#     4               V = 4
#     6               arr[] size n = 6 (not passed, see function description parameters)
#     1 4 5 7 9 12    arr = [1, 4, 5, 7, 9, 12]

# Sample Output 0
#     1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#


def introTutorial(V: int, arr: list) -> int:
    # Write your code here
    value = arr.index(V)
    return value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
