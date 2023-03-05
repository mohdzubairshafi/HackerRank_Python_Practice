# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


# solution
if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    score = list(arr)
    score.sort(reverse=(True))
    maxele = score[0]
    for i in score:
        if i != maxele:
            print(i)
            break
