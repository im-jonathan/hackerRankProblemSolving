# Little Bobby loves chocolate. He frequently goes to his favorite 5 & 10 store, Penny Auntie, to buy them. They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.
# Example
# n = 15
# c = 3
# m = 2

# He has 15 to spend, bars cost 3, and he can turn in 2 wrappers to receive another bar. Initially, he buys 5 bars and has 5 wrappers after eating them. He turns in 4 of them, leaving him with 1, for 2 more bars. After eating those two, he has 3 wrappers, turns in 2 leaving him with 1 wrapper and his new bar. Once he eats that one, he has 2 wrappers and turns them in for another bar. After eating that one, he only has 1 wrapper, and his feast ends. Overall, he has eaten 5+2+1+1=9 bars.

# Function Description
# Complete the chocolateFeast function in the editor below.

# chocolateFeast has the following parameter(s):
# - int n: Bobby's initial amount of money
# - int c: the cost of a chocolate bar
# - int m: the number of wrappers he can turn in for a free bar

# Returns
# int: the number of chocolates Bobby can eat after taking full advantage of the promotion
# Note: Little Bobby will always turn in his wrappers if he has enough to get a free chocolate.

# Input Format
# The first line contains an integer, t, the number of test cases to analyze.
# Each of the next t lines contains three space-separated integers: n, c, and m. They represent money to spend, cost of a chocolate, and the number of wrappers he can turn in for a free chocolate.

# Constraints
# 1 ≤ t ≤ 1000
# 2 ≤ n ≤ 10^5
# 1 ≤ c ≤ n
# 2 ≤ m ≤ n

# Sample Input
#     STDIN   Function
#     ----- --------
#     3       t = 3 (test cases)
#     10 2 5  n = 10, c = 2, m = 5 (first test case)
#     12 4 4  n = 12, c = 4, m = 4 (second test case)
#     6 2 2   n = 6,  c = 2, m = 2 (third test case)

# Sample Output
#     6
#     3
#     5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#


def chocolateFeast(n: int, c: int, m: int) -> int:
    # Write your code here
    wrapper = n/c
    choc_count = int(wrapper)
    while wrapper >= m:
        wrapper -= m
        wrapper += 1
        choc_count += 1
    return choc_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
