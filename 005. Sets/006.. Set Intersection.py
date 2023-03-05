# Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


englishStudents = int(input())
EnglishSet = set(map(int, input().split()))
frenchStudents = int(input())
frenchSet = set(map(int, input().split()))

result = EnglishSet.intersection(frenchSet)

print(len(result))
