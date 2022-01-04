# Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring "010".
# In one step, Alice can change a 0 to a 1 or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.
# Example
# b = 010
# She can change any one element and have a beautiful string.

# Function Description
# Complete the beautifulBinaryString function in the editor below.
# beautifulBinaryString has the following parameter(s):
# - string b: a string of binary digits

# Returns
# int: the minimum moves required

# Input Format
# The first line contains an integer n, the length of binary string.
# The second line contains a single binary string b.

# Constraints
# 1 ≤ n ≤ 100
# b[i] ∈ {0,1}.

# Output Format
# Print the minimum number of steps needed to make the string beautiful.

# Sample Input 0
#     STDIN       Function
#     ----- --------
#     7           length of string n = 7
#     0101010     b = '0101010'

# Sample Output 0
#     2

# Sample Input 1
# 5
# 01100

# Sample Output 1
#     0

# Sample Input 2
#     10
#     0100101010
# Sample Output 2
#     3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#


def beautifulBinaryString(b: str) -> int:
    # Write your code here
    return b.count('010')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
