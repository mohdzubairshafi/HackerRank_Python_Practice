# problem: https://www.hackerrank.com/challenges/py-set-add/problem

N = int(input())
stamp_set = set()
for i in range(N):
    stamp = input()
    stamp_set.add(stamp)
print(len(stamp_set))
