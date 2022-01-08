# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
# Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over all n days.
# Example
# expenditure = [10,20,30,40,50]
# d = 3
# On the first three days, they just collect spending data. At day 4, trailing expenditures are[10, 20, 30]. The median is 20 and the day's expenditure is 40. Because 40 ≥ 2x20, there will be a notice. The next day, trailing expenditures are [20,30,40] and the expenditures are 50. This is less than 2x20 so no notice will be sent. Over the period, there was one notice sent.
# Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two middle values. (Wikipedia)

# Function Description
# Complete the function activityNotifications in the editor below.
# activityNotifications has the following parameter(s):
# - int expenditure[n]: daily expenditures
# - int d: the lookback days for median spending

# Returns
# int: the number of notices sent

# Input Format
# The first line contains two space-separated integers n and d, the number of days of transaction data, and the number of trailing days' data used to calculate median spending respectively.
# The second line contains n space-separated non-negative integers where each integer i denotes expenditure[i].

# Constraints
# 1 ≤ n ≤ 2x10^5
# 1 ≤ d ≤ n
# 0 ≤ expenditure[i] ≤ 200

# Output Format
# Sample Input 0
#     STDIN               Function
#     ----- --------
#     9 5                 expenditure[] size n = 9, d = 5
#     2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

# Sample Output 0
#     2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure: list, d: int) -> int:
    # Write your code here
    freq = {}
    notify = 0

    def find(idx: int) -> int:
        total_count = 0
        for i in range(201):
            if i in freq:
                total_count += freq[i]
            if total_count >= idx:
                return i
    for i in range(len(expenditure)-1):
        if expenditure[i] in freq:
            freq[expenditure[i]] += 1
        else:
            freq[expenditure[i]] = 1
        #print(f"i: {i},val: {expenditure[i]}, freq: {freq}")
        if i >= d-1:
            if d % 2 == 0:
                median = (find(d//2)+find(d//2+1))/2
            else:
                median = find(d/2)
            #print("median: ",median)
            if expenditure[i+1] >= (median*2):
                notify += 1
                # print("notify: ",notify)
            #remove the previous element from dictionary
            freq[expenditure[i-d+1]] -= 1

    return notify


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
