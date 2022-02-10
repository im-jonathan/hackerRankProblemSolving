# A palindrome is a string that reads the same from left to right as it does from right to left.
# Given a string, S, of N lowercase English letters, we define a k-length rotation as cutting the first k characters from the beginning of S and appending them to the end of S. For each S, there are N possible k-length rotations(where 0 ≤ k < N). See the Explanation section for examples.
# Given N and S, find all N k-length rotations of S for each rotated string, Sk, print the maximum possible length of any palindromic substring of Sk on a new line.

# Input Format
# The first line contains an integer, N (the length of S).
# The second line contains a single string, S.

# Constraints
# 1 ≤ N ≤ 5x10^5
# 0 ≤ k < N
# S is comprised of lowercase English letters.

# Output Format
# There should be N lines of output, where each line k contains an integer denoting the maximum length of any palindromic substring of rotation Sk.

# Sample Input 0
#     13
#     aaaaabbbbaaaa

# Sample Output 0
#     12
#     12
#     10
#     8
#     8
#     9
#     11
#     13
#     11
#     9
#     8
#     8
#     10

# Sample Input 1
#     7
#     cacbbba

# Sample Output 1
#     3
#     3
#     3
#     3
#     3
#     3
#     3

# Sample Input 2
#     12
#     eededdeedede

# Sample Output 2
#     5
#     7
#     7
#     7
#     7
#     9
#     9
#     9
#     9
#     7
#     5
#     4

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularPalindromes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING s as parameter.
#


def circularPalindromes(s: str) -> list:
    # Write your code here
    container = []
    org = []
    contain = []
    ego = []
    conca = len(s)
    b = 3 * s
    curchar = '\0'
    curstart = 0
    curcount = 0
    let = []
    tripstart = 0
    for i, c in enumerate(b):
        #what it really does it to give the character, number of times it appeared in a streak
        #the 0 index gives the character, the 1st gives the no of times in a go(streak)
        #the third gives the index of the character at which the streak begins.
        if not i:
            curstart = 0
            curcount = 1
            curchar = c
        else:
            if c == curchar:
                curcount += 1
            else:
                for j in range(curcount):
                    let.append((curchar, curcount, curstart))
                curstart = i
                curcount = 1
                curchar = c
    for i in range(curcount):
        let.append((curchar, curcount, curstart))
    for i in range(conca):
        c = conca + i
        part = -1
        if let[c][1] % 2 and c == let[c][2] + let[c][1]//2:
            #This is to expand around the body of the streak if the streak
            #is odd in length and if the center c falls in the middle of the streak
            #then expansion will occur in bursts alays limited by the minimum one of course.
            inner = let[c][1]
            mud = i
            part = let[c][1]
            p1 = let[c][2] - 1
            p2 = let[c][2] + let[c][1]
            while p1 >= 0 and p2 < 3*conca and let[p1][0] == let[p2][0]:
                if let[p1][1] != let[p2][1]:
                    #if they are not congrous anymore, the minimum limits
                    part += 2*min(let[p1][1], let[p2][1])
                    break
                part += 2*let[p1][1]
                p1 -= let[p1][1]
                p2 += let[p2][1]
            tit = part
            org.append((tit, mud, inner))
        else:
            #if even or (odd without the streak having its center at that c)
            part = 1 + 2*min(c-let[c][2], let[c][2] + let[c][1] - 1 - c)
            #The first part of the minimum deals with the distance
            #between the index c and the beginning of the streak
            #the second part deals with distance from the center to the end of the streak.
        container.append(min(conca, part))

        egg = 0
        if let[c][1] % 2 == 0 and c == let[c][2] + let[c][1]//2:
            '''This deals with expanding about even numbers, the first condition indicate
            the streak must be even in length, the 2nd says it must be one beyond the 
            'invisible' middle, and then everything is similar in retrospect to the one above
            '''
            inn = let[c][1]
            mid = i
            egg = let[c][1]
            p1 = let[c][2] - 1
            p2 = let[c][2] + let[c][1]
            while p1 >= 0 and p2 < 3*conca and let[p1][0] == let[p2][0]:
                if let[p1][1] != let[p2][1]:
                    egg += 2*min(let[p1][1], let[p2][1])
                    break
                egg += 2*let[p1][1]
                p1 -= let[p1][1]
                p2 += let[p2][1]
            tat = egg
            ego.append((tat, mid, inn))
        else:
            '''This deals with even numbers and odd numbers-those which cannot satisfy the
            2nd if condition, it must be noted that only one index per streak can satisfy that.
            '''
            egg = 2 + 2*min(c - 1 - let[c][2], let[c][2] + let[c][1] - 1 - c)
        contain.append(min(conca, egg))
    rock = sorted(org, key=lambda x: x[0], reverse=True)
    wrec = sorted(ego, key=lambda x: x[0], reverse=True)
    bests = []
    if conca % 2:
        bests = [max(container[(i+conca//2) % conca], min(conca-1, max(contain[(i+conca//2) %
                     conca], contain[(i+conca//2+1) % conca]))) for i in range(conca)]
    else:
        bests = [max(contain[(i+conca//2) % conca], min(conca-1, max(container[(i+conca//2) %
                     conca], container[(i+conca//2-1) % conca]))) for i in range(conca)]
    for i in range(conca):
        top = bests[i]
        rosi = 0
        while(rosi < len(rock) and rock[rosi][0] > top):
            res = min(rock[rosi][0], 1+2*min((rock[rosi][1]-i) %
                      conca, (i - 1 - rock[rosi][1]) % conca))
            if res < rock[rosi][2]:
                res = min(rock[rosi][2], max((i - (rock[rosi][1] - rock[rosi][2]//2)) %
                          conca, (rock[rosi][1] + rock[rosi][2]//2 + 1 - i) % conca))
            top = max(top, min(res, conca))
            rosi += 1
        resi = 0
        while(resi < len(wrec) and wrec[resi][0] > top):
            res = min(wrec[resi][0], 2*min((wrec[resi][1]-i) %
                      conca, (i - wrec[resi][1]) % conca))
            if res < wrec[resi][2]:
                res = min(wrec[resi][2], max((i - (wrec[resi][1] - wrec[resi][2]//2)) %
                          conca, (wrec[resi][1] + wrec[resi][2]//2 - i) % conca))
            top = max(top, min(res, conca))
            resi += 1
        bests[i] = top
    return bests


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    result = circularPalindromes(s)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
