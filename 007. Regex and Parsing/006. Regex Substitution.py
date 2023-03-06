# Problem: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

n = int(input())
for i in range(n):
    line = input()
    remove_and = re.sub(r"(?<= )(&&)(?= )", "and", line)
    remove_or = re.sub(r"(?<= )(\|\|)(?= )", "or", remove_and)
    print(remove_or)
