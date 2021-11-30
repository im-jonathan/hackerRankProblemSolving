# Larry has been given a permutation of a sequence of natural numbers incrementing from 1 as an array. He must determine whether the array can be sorted using the following operation any number of times:
# Choose any 3 consecutive indices and rotate their elements in such a way that ABC -> BCA -> CAB -> ABC.
# For example, if A = {1, 6, 5, 2, 4, 3}:

#     A		        rotate
# [1, 6, 5, 2, 4, 3]  [6, 5, 2]
# [1, 5, 2, 6, 4, 3]  [5, 2, 6]
# [1, 2, 6, 5, 4, 3]  [5, 4, 3]
# [1, 2, 6, 3, 5, 4]  [6, 3, 5]
# [1, 2, 3, 5, 6, 4]  [5, 6, 4]
# [1, 2, 3, 4, 5, 6]

# YES
# On a new line for each test case, print YES if A can be fully sorted. Otherwise, print NO.

# Function Description
# Complete the larrysArray function in the editor below. It must return a string, either YES or NO.
# larrysArray has the following parameter(s):
# - A: an array of integers

# Input Format
# The first line contains an integer t, the number of test cases.
# The next t pairs of lines are as follows:
# The first line contains an integer n, the length of A.
# The next line contains n space-separated integers A[i].

# Constraints
# 1 ≤ t ≤ 10
# 3 ≤ n ≤ 1000
# 1 ≤ A[i] ≤ n
# Asorted = integers that increment by 1 from 1 to n

# Output Format
# For each test case, print YES if A can be fully sorted. Otherwise, print NO.

# Sample Input
#     3
#     3
#     3 1 2
#     4
#     1 3 4 2
#     5
#     1 2 3 5 4

# Sample Output
#     YES
#     YES
#     NO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#


def larrysArray(A: list) -> str:
    # Write your code here
    for i in range(n-2):
        for x in range(n-2):
            c = 0
            while True:
                #if the first element of the group is min then it's sortable
                if A[x] == min(A[x], A[x+1], A[x+2]):
                    break

                #if we can't sort the group after 2 rotate it's not possible to sort
                if c == 2:
                    return 'NO'

                #rotate elements
                i, j, k = A[x:x+3]
                A[x:x+3] = k, i, j

                c += 1

    #need to check if something like 2,4,3 on the end
    return 'YES' if A[-3:] == sorted(A[-3:]) else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
