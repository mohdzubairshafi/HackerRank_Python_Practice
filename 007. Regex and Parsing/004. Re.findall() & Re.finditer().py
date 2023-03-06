# Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem


import re

string = input()
pattern = r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])"
result = re.findall(pattern, string)
if result:
    for i in result:
        print(i)
else:
    print(-1)
