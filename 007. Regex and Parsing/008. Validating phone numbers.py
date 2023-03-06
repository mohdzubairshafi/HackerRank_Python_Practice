# Problem: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())
for _ in range(n):
    phone_number = input()
    condition = r"^[7-9]\d{9}$"
    if bool(re.match(condition, phone_number)):
        print("YES")
    else:
        print("NO")
