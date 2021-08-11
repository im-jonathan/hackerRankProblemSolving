# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time(arrivalTime ≤ 0) to arrived late(arrivvalTime > 0).
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.
# Example
# n = 5
# k = 3
# a = [-2, -1- 0, 1, 2]

# The first 3 students arrived on. The last 2 were late. The threshold is 3 students, so class will go on. Return YES.
# Note: Non-positive arrival times(a[i] ≤ 0) indicate the student arrived early or on time
# positive arrival times(a[i] > 0) indicate the student arrived a[i] minutes late.

# Function Description
# Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.
# angryProfessor has the following parameter(s):
# - int k: the threshold number of students
# - int a[n]: the arrival times of the  students

# Returns
# string: either YES or NO

# Input Format
# The first line of input contains t, the number of test cases.
# Each test case consists of two lines.
# The first line has two space-separated integers, n and k, the number of students (size of a) and the cancellation threshold.
# The second line contains n space-separated integers(a[1], a[2]...a[n]) that describe the arrival times for each student.

# Constraints
# 1 ≤ t ≤ 10
# 1 ≤ n ≤ 1000
# 1 ≤ k ≤ n
# -100 ≤ a[i] ≤ 100, where i ∈ [1...n]

# Sample Input
#     2
#     4 3
#     -1 - 3 4 2
#     4 2
#     0 - 1 2 1
# Sample Output
#     YES
#     NO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#


def angryProfessor(k, a):
    # Write your code here
    students_ontime = [i for i in a if i <= 0]
    if len(students_ontime) >= k:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
