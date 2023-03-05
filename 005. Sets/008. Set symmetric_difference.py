# Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

englishStudents = int(input())
EnglishSet = set(map(int, input().split()))
frenchStudents = int(input())
frenchSet = set(map(int, input().split()))

result = EnglishSet.symmetric_difference(frenchSet)

print(len(result))
