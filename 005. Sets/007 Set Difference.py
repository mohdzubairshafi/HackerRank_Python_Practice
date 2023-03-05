# Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem


englishStudents = int(input())
EnglishSet = set(map(int, input().split()))
frenchStudents = int(input())
frenchSet = set(map(int, input().split()))

result = EnglishSet.difference(frenchSet)

print(len(result))
