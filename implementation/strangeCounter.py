# There is a strange counter. At the first second, it displays the number 3. Each second, the number displayed by decrements by 1 until it reaches 1. In next second, the timer resets to 2 x the initial number for the period cicle and continues counting down. The diagram below shows the counter values for each time in the first three cycles.

# Find and print the value displayed by the counter at time t.

# Function Description
# Complete the strangeCounter function in the editor below.

# strangeCounter has the following parameter(s):
# - int t: an integer

# Returns
# int: the value displayed at time

# Input Format
# A single integer, the value of t.

# Constraints
# 1 ≤ t ≤ 10^12
# Subtask
# 1 ≤ t ≤ 10^5 for 60% of the maximum score.

# Sample Input
#     4

# Sample Output
#     6

# Explanation
# Time t=4 marks the beginning of the second cycle. It is double the number displayed at the beginning of the first cycle: 2x3=6. This is shown in the diagram in the problem statement.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#


def strangeCounter(t: int) -> int:
    # Write your code here
    n = 0
    count = 0
    while n < t:
        n += 3*(2**count)
        count += 1
    result = n-t+1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
