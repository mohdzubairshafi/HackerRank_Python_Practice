N, M = map(int, input().split())

design = ".|."
lowerHalf = 0
for i in range(N):
    if i < N // 2:
        print((design * (2 * i + 1)).center(M, "-"))
    if i == N // 2:
        print("WELCOME".center(M, "-"))
for i in range(N // 2, 0, -1):
    print((design * (2 * i - 1)).center(M, "-"))
