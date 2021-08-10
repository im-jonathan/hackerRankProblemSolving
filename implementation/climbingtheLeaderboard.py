# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
# - The player with the highest score is ranked number  on the leaderboard.
# - Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# Example
# ranked = [100,90,90,80]
# player = [70,80,105]
# The ranked players will have ranks 1, 2, 2, and 3, respectively. If the player's scores are 70, 80 and 105, their rankings after each game are 4th, 3rd and 1st. Return [4,3,1].

# Function Description
# Complete the climbingLeaderboard function in the editor below.
# climbingLeaderboard has the following parameter(s):
# - int ranked[n]: the leaderboard scores
# - int player[m]: the player's scores

# Returns
# int[m]: the player's rank after each new score

# Input Format
# The first line contains an integer n, the number of players on the leaderboard.
# The next line contains n space-separated integers ranked[i], the leaderboard scores in decreasing order.
# The next line contains an integer, m, the number games the player plays.
# The last line contains  space-separated integers player[j], the game scores.

# Constraints
# 1 ≤ n ≤ 2 * 10^5
# 1 ≤ m ≤ 2 * 10^5
# 0 ≤ ranked[i] ≤ 10^9 for 0 ≤ i < n
# 0 ≤ player[j] ≤ 10^9 for 0 ≤ i < m

# The existing leaderboard, ranked, is in descending order.
# The player's scores, player, are in ascending order.

# Subtask
# For 60% of the maximum score:
# 1 ≤ n ≤ 200
# 1 ≤ m ≤ 200

# Sample Input 1
#     7
#     100 100 50 40 40 20 10
#     4
#     5 25 50 120

# Sample Output 1
#     6
#     4
#     2
#     1

# Sample Input 2
#     6
#     100 90 90 80 75 60
#     5
#     50 65 77 90 102

# Sample Output 2
#     6
#     5
#     4
#     2
#     1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    leaderboard = sorted(set(ranked), reverse = True)
    l = len(leaderboard)
    data = []

    for a in player:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        data.append(l+1)
    return data

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
