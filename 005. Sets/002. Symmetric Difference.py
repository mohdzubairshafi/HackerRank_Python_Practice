# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
setM = set(map(int, input().split()))
N = int(input())
setN = set(map(int, input().split()))

diff_M_N = setM.difference(setN)
diff_N_M = setN.difference(setM)

result =  sorted(diff_M_N.union(diff_N_M) , key=int) 

print(*result, sep='\n')

