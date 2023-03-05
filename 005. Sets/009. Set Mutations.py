# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem

N = int(input())
setA = set(map(int, input().split()))
no_of_sets = int(input())

for i in range(no_of_sets):
    command = list(input().split())
    command_set = set(map(int, input().split()))
    expression = f"setA.{command[0]}(command_set)"
    eval(expression)

print(sum(setA))
