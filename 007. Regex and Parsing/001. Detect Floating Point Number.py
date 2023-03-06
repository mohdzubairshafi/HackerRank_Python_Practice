# Problem: https://www.hackerrank.com/challenges/introduction-to-regex/problem


import re

pattern = r"[+-]{0,1}\d*\.\d+$"

T = int(input())
matchs = [False] * T
for i in range(T):
    string = input()
    if re.match(pattern, string):
        matchs[i] = True
print(*matchs, sep="\n")
