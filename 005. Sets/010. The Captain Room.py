# problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem

K = int(input())
roomList = list(map(int, input().split()))
mp = dict()

for i in range(len(roomList)):
    if roomList[i] in mp.keys():
        mp[roomList[i]] += 1
    else:
        mp[roomList[i]] = 1

for x in mp:
    if mp[x] == 1:
        print(x)
