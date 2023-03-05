# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


n = int(input())
s = set(map(int, input().split()))
no_of_commands = int(input())

for i in range(no_of_commands):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))

sm = 0
for i in s:
    sm += i
print(sm)
