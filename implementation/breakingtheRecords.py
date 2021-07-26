# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Example
# scores = [12, 24, 10, 24]
# Scores are in the same order as the games played. She tabulates her results as follows:
#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1

# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

# Function Description
# Complete the breakingRecords function in the editor below.

# breakingRecords has the following parameter(s):
# - int scores[n]: points scored per game

# Returns
# - int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
# Input Format

# The first line contains an integer n, the number of games.
# The second line contains n space-separated integers describing the respective values of score1, score2, ... scoren-1.

# Constraints
# 1 ≤ n ≤ 1000
# 0 ≤ scores[i] ≤ 10^8

# Sample Input 0
#     9
#     10 5 20 20 4 5 2 25 1

# Sample Output 0
#     2 4

# Sample Input 1
#     10
#     3 4 21 36 10 28 35 5 24 42

# Sample Output 1
#     4 0

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min = scores[0]
    max = scores[0]
    min_count = 0
    max_count = 0
    for score in scores[1:]:
        if score > max:
            max_count += 1
            max = score
        if score < min:
            min_count += 1
            min = score
    return max_count, min_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
