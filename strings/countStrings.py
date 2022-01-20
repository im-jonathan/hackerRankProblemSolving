# A regular expression is used to describe a set of strings. For this problem the alphabet is limited to 'a' and 'b'.
# We define R to be a valid regular expression if:
# 1) R is "a" or "b".
# 2) R is of the form "(R1 R2)", where R1 and R2 are regular expressions.
# 3) R is of the form "(R2|R2)" where R1 and R2 are regular expressions.
# 4) R is of the form "(R1*)" where R1 is a regular expression.
# Regular expressions can be nested and will always have have two elements in the parentheses. ('*' is an element, '|' is not; basically, there will always be pairwise evaluation) Additionally, '*' will always be the second element; '(*a)' is invalid.
# The set of strings recognized by R are as follows:
# 1) If R is "a", then the set of strings recognized = a.
# 2) If R is "b", then the set of strings recognized =b.
# 3) If R is of the form "(R1 R2)" then the set of strings recognized = all strings which can be obtained by a concatenation of strings s1 and s2, where s1 is recognized by R1 and s2 by R2.
# 4) If R is of the form "(R1|R2)" then the set of strings recognized = union of the set of strings recognized by R1 and R2.
# 5) If R is of the form "(R1*)" then the the strings recognized are the empty string and the concatenation of an arbitrary number of copies of any string recognized by R1.

# Task
# Given a regular expression and an integer, L, count how many strings of length L are recognized by it.

# Input Format
# The first line contains the number of test cases T. T test cases follow.
# Each test case contains a regular expression, R, and an integer, L.

# Constraints
# 1 ≤ T ≤ 50
# 1 ≤ |R| ≤ 100
# 1 ≤ L ≤ 10^9
# It is guaranteed that R will conform to the definition provided above.

# Output Format
# Print T lines, one corresponding to each test case containing the required answer for the corresponding test case. As the answers can be very big, output them modulo 10^9 + 7.

# Sample Input
#     3  
#     ((ab)|(ba)) 2  
#     ((a|b)*) 5  
#     ((a*)(b(a*))) 100

# Sample Output
#     2  
#     32  
#     100

#!/usr/bin/python
from collections import defaultdict

START = 2
FINAL = 3
SPLIT = 4
DANGLING = 0
MOD = 1000000007


class State(object):
    def __init__(self, c, out=None, out1=None):
        self.c = c  # 0: 'a', 1: 'b':, 2: start, 3: final, 4: split
        self.out = out  # None for NULL, 0 for dangling
        self.out1 = out1  # None for NULL, 0 for dangling


class Frag(object):
    def __init__(self, start, outs):
        self.start = start
        self.outs = outs

    def patch(self, s):
        for x in self.outs:
            if x.out == DANGLING:
                x.out = s
            if x.out1 == DANGLING:
                x.out1 = s

    def append(self, a):
        self.outs.extend(a)
        return self.outs


class Regex(object):
    def __init__(self, s):
        self.s = s
        self.cur = 0
        self.trans = defaultdict(list)
        self.mapping = {}
        self.finals = []

    def single(self, c):
        s = State(c, DANGLING)
        return Frag(s, [s])

    def cat(self, a, b):
        a.patch(b.start)
        return Frag(a.start, b.outs)

    def alt(self, a, b):
        s = State(SPLIT, a.start, b.start)
        return Frag(s, a.append(b.outs))

    def star(self, a):
        s = State(SPLIT, a.start, DANGLING)
        a.patch(s)
        return Frag(s, [s])

    def parse(self):
        c = self.s[self.cur]
        self.cur += 1
        if c == '(':
            a = self.parse()
            c = self.s[self.cur]
            if c == '*':  # star
                self.cur += 2  # "*)"
                return self.star(a)
            elif c == '|':  # alternative
                self.cur += 1  # '|'
                b = self.parse()
                self.cur += 1  # ')'
                return self.alt(a, b)
            else:  # cat
                b = self.parse()
                self.cur += 1  # ')'
                return self.cat(a, b)
        else:  # 'a' or 'b':
            if c == 'a':
                return self.single(0)
            else:
                return self.single(1)

    def move(self, ss, s, checked):
        if s in checked:
            return
        checked.add(s)
        ss.add(s)
        if s.c == SPLIT:
            ss.remove(s)
            if s.out is not None:
                self.move(ss, s.out, checked)
            if s.out1 is not None:
                self.move(ss, s.out1, checked)

    def dfa(self, ss, parent=-1):
        # move forward if possible
        save = list(ss)
        checked = set()
        for s in save:
            self.move(ss, s, checked)
        key = tuple(ss)
        # check if computed
        if key in self.mapping:
            if parent >= 0:
                self.trans[parent].append(self.mapping[key])
            return
        # record final states
        gid = len(self.mapping)
        self.mapping[key] = gid
        for x in key:
            if x.c == FINAL:
                self.finals.append(gid)
                break
        if parent >= 0:
            self.trans[parent].append(gid)
        # go sub
        to = [set(), set()]
        for s in ss:
            if s.c <= 1:
                if s.out is not None:
                    to[s.c].add(s.out)
                if s.out1 is not None:
                    to[s.c].add(s.out1)
        for t in to:
            if len(t) > 0:
                self.dfa(t, gid)

    def graph(self):
        n = len(self.mapping)
        ret = [[0] * n for x in range(n)]
        visited = [False] * n

        def dfs(now):
            if visited[now] or now not in self.trans:
                return
            visited[now] = True
            for v in self.trans[now]:
                ret[now][v] += 1
                dfs(v)
        for x in self.trans:
            dfs(x)
        return ret


def mul(a, b):
    n = len(a)
    c = [[0] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= MOD
    return c


def power(a, n):
    if n == 1:
        return a
    ret = power(a, n // 2)
    ret = mul(ret, ret)
    if n & 1:
        ret = mul(ret, a)
    return ret


n = int(input())
for x in range(n):
    r, l = input().strip().split()
    l = int(l)
    reg = Regex(r)
    frag = reg.parse()
    frag.patch(State(FINAL))
    reg.dfa(set([frag.start]))
    graph = reg.graph()
    graph = power(graph, l)
    ans = 0
    for f in reg.finals:
        ans += graph[0][f]
    print(ans % MOD)
