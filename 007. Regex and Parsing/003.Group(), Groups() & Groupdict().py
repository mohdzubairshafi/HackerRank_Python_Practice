# Problem: https://www.hackerrank.com/challenges/re-group-groups/problem


import re

string = input()
pattern = r"([A-Za-z0-9])\1"
res = re.search(pattern, string)
if res is None:
    print(-1)
else:
    print(res[1])
