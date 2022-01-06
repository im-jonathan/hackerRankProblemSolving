# Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of shifts an insertion sort performs when sorting an array?
# If k[i] is the number of elements over which the ith element of the array has to shift, then the total number of shifts will be k[1]+k[2]+...+k[n].
# Example
# arr = [4,3,2,1]
# Array		Shifts
# [4, 3, 2, 1]
# [3, 4, 2, 1]	1
# [2, 3, 4, 1]	2
# [1, 2, 3, 4]	3
# Total shifts = 1 + 2 + 3 = 6

# Function description
# Complete the insertionSort function in the editor below.
# insertionSort has the following parameter(s):
# - int arr[n]: an array of integers

# Returns
# - int: the number of shifts required to sort the array

# Input Format
# The first line contains a single integer t, the number of queries to perform.
# The following t pairs of lines are as follows:
# The first line contains an integer n, the length of arr.
# The second line contains n space-separated integers arr[i].

# Constraints
# 1 ≤ t ≤ 15
# 1 ≤ n ≤ 100000
# 1 ≤ a[i] ≤ 10000000

# Sample Input
#     2
#     5
#     1 1 1 2 2
#     5
#     2 1 3 1 2

# Sample Output
#     0
#     4

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def insertionSort(arr: list) -> int:
    # Write your code here
    l = len(arr)
    if l == 1:
        return 0
    m = l//2
    n = l - m
    a1 = arr[:m]
    a2 = arr[m:]
    ans = insertionSort(a1) + insertionSort(a2)
    count1 = 0
    count2 = 0
    for i in range(l):
        if count1 < m and (count2 >= n or a1[count1] <= a2[count2]):
            arr[i] = a1[count1]
            ans += count2
            count1 += 1
        elif count2 < n:
            arr[i] = a2[count2]
            count2 += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
