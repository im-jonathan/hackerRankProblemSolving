# Challenge
# Can you modify your previous Insertion Sort implementation to keep track of the number of shifts it makes while sorting? The only thing you should print is the number of shifts made by the algorithm to completely sort the array. A shift occurs when an element's position changes in the array. Do not shift an element if it is not necessary.

# Function Description
# Complete the runningTime function in the editor below.
# runningTime has the following parameter(s):
# - int arr[n]: an array of integers

# Returns
# int: the number of shifts it will take to sort the array

# Input Format
# The first line contains the integer n, the number of elements to be sorted.
# The next line contains n integers of arr[arr[0]...arr[n-1]].

# Constraints
# 1 ≤ n ≤ 1001
# -10000 ≤ arr[i] ≤ 10000, where i ∈ {0...(n-1)}

# Sample Input
#     STDIN       Function
#     ----- --------
#     5           arr[] size n = 5
#     2 1 3 1 2   arr = [2, 1, 3, 1, 2]

# Sample Output
#     4

# Explanation
# Iteration   Array      Shifts
# 0           2 1 3 1 2
# 1           1 2 3 1 2     1
# 2           1 2 3 1 2     0
# 3           1 1 2 3 2     2
# 4           1 1 2 2 3     1

# Total                     4

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def runningTime(arr: list) -> int:
    # Write your code here
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
