# Problem : https://www.hackerrank.com/challenges/python-power-mod-power/problem

import math

a = int(input())
b = int(input())
m = int(input())

print(round(math.pow(a, b)))
print(pow(a, b, m))
