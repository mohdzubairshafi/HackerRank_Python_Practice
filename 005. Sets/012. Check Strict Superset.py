# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem


setA = set(input().split())
flag = True
for i in range(int(input())):
    setB = set(input().split())
    if not (setA > setB):
        flag = False
        break
print(flag)
