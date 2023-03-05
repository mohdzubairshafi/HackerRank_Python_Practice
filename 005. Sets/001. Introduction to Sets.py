# Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    # your code goes here
    distinct_heights_set = set(array)

    sm = 0
    for height in distinct_heights_set:
        sm += height

    return sm / len(distinct_heights_set)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
