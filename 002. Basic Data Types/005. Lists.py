# Problem: https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == "__main__":
    myList = []
    N = int(input())
    for _ in range(N):
        inp = input().split()
        command = inp[0]
        value = inp[1:]
        if command == "print":
            print(myList)
        else:
            expression = f"myList.{command}({','.join(value)})"
            eval(expression)
