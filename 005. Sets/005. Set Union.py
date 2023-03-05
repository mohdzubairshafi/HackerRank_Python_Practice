# Problem: https://www.hackerrank.com/challenges/py-set-union/problem

englishStudents = int(input())
EnglishSet = set(map(int, input().split()))
frenchStudents = int(input())
frenchSet = set(map(int, input().split()))

result = EnglishSet.union(frenchSet)

print(len(result))
