# You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread. Your subjects are in a line, and some of them already have some loaves. Times are hard and your castle's food stocks are dwindling, so you must distribute as few loaves as possible according to the following rules:
# 1. Every time you give a loaf of bread to some person i, you must also give a loaf of bread to the person immediately in front of or behind them in the line (i.e., persons i + 1 or i - 1).
# 2. After all the bread is distributed, each person must have an even number of loaves.
# Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute to satisfy the two rules above. If this is not possible, print NO.

# Example
# B = [4,5,6,7]
# We can first give a loaf to i=3 and i=4 so B=[4,5,7,8].
# Next we give a loaf to i=2 and i=3 and have B=[4,6,8,8] which satisfies our conditions.
# All of the counts are now even numbers. We had to distribute 4 loaves.

# Function Description
# Complete the fairRations function in the editor below.

# fairRations has the following parameter(s):
# - int B[N]: the numbers of loaves each persons starts with

# Returns
# string: the minimum number of loaves required, cast as a string, or 'NO'

# Input Format
# The first line contains an integer N, the number of subjects in the bread line.
# The second line contains N space-separated integers B[i].

# Constraints
# 2 ≤ N ≤ 1000
# 1 ≤ B[i] ≤ 10, where 1 ≤ i ≤ N

# Output Format
# Sample Input 0
#     STDIN       Function
#     ----- --------
#     5           B[] size N = 5
#     2 3 4 5 6   B = [2, 3, 4, 5, 6]

# Sample Output 0
#     4

# Sample Input 1
#     2
#     1 2

# Sample Output 1
#     NO

#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Union

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#


def fairRations(B: list) -> str:
    # Write your code here
    count = 0
    for a in range(len(B)):
        try:
            if B[a] % 2 == 1:
                count += 2
                B[a+1] += 1
        except:
            return 'NO'
    return str(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
