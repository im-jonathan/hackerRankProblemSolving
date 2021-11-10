# Given the time in numerals we may convert it into words, as shown below:
#     5:00 -> five o' clock
#     5:01 -> one minute past five
#     5:10 -> ten minutes past five
#     5:15 -> quarter past five
#     5:30 -> half past five
#     5:40 -> twenty minutes to six
#     5:45 -> quarter to six
#     5:47 -> thirteen minutes to six
#     5:28 -> twenty eight minutes past five

# At minutes = 0, use o' clock. For 1 ≤ minutes ≤ 30 , use past, and for 30 < minutes use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

# Function Description
# Complete the timeInWords function in the editor below.

# timeInWords has the following parameter(s):
# - int h: the hour of the day
# - int m: the minutes after the hour

# Returns
# string: a time string as described

# Input Format
# The first line contains h, the hours portion The second line contains m, the minutes portion

# Constraints
# 1 ≤ h ≤ 12
# 0 ≤ m < 60

# Sample Input 0
#     5
#     47

# Sample Output 0
#     thirteen minutes to six

# Sample Input 1
#     3
#     00

# Sample Output 1
#     three o' clock

# Sample Input 2
#     7
#     15

# Sample Output 2
#     quarter past seven

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#


def timeInWords(h: int, m: int) -> str:
    # Write your code here
    hours = ("one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve"
    )
    minutes = ("one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "ninteen", "twenty", "twenty one", "twenty two",
        "twenty three", "twenty four", "twenty five", "twenty six",
        "twenty seven", "twenty eight", "twenty nine"
    )

    formats = {
        0: "%s o' clock",
        1: "one minute past %s",
        10: "ten minutes past %s",
        15: "quarter past %s",
        30: "half past %s",
        40: "twenty minutes to %s",
        45: "quarter to %s",
    }

    time = ""

    if m in (0, 1, 10, 15, 30, 40, 45):
        k = 1 if m <= 30 else 0
        time = formats[m] % hours[h - k]

    elif (m < 30):
        hour = hours[h - 1]
        time = f"{minutes[m - 1]} minutes past {hour}"

    elif (m > 30):
        hour = hours[h]
        time = f"{minutes[60 - m - 1]} minutes to {hour}"

    return time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
