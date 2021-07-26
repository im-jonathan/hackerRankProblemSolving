# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# - The length of the segment matches Ron's birth month, and,
# - The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# Example
# s = [2,2,1,3,2]
# d = 4
# m = 2

# Lily wants to find segments summing to Ron's birth day, d=4 with a length equalling his birth month, m=2. In this case, there are two segments meeting her criteria: [2,2] and [1,3].

# Function Description
# Complete the birthday function in the editor below.
# birthday has the following parameter(s):
# - int s[n]: the numbers on each of the squares of chocolate
# - int d: Ron's birth day
# - int m: Ron's birth month

# Returns
# - int: the number of ways the bar can be divided

# Input Format
# The first line contains an integer n, the number of squares in the chocolate bar.
# The second line containsn  space-separated integers s[i], the numbers on the chocolate squares where 0 ≤ i < n.
# The third line contains two space-separated integers, d and m, Ron's birth day and his birth month.

# Constraints
# 1 ≤ n ≤ 100
# 1 ≤ s[i] ≤ 5, where(0 ≤ i < n)
# 1 ≤ d ≤ 31
# 1 ≤ m ≤ 12

# Sample Input 0
#     5
#     1 2 1 3 2
#     3 2

# Sample Output 0
#     2

# Sample Input 1
#     6
#     1 1 1 1 1 1
#     3 2

# Sample Output 1
#     0

# Sample Input 2
#     1
#     4
#     4 1

# Sample Output 2
#     1
    
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(0, len(s)+1-m):
        if sum(s[i:i+m]) == d:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

