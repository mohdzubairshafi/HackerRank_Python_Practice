# Problem: https://www.hackerrank.com/challenges/capitalize/problem

import os


def solve(s):
    result = ""
    for i in range(0, len(s)):
        if i == 0:
            result = result + (s[i].upper())
        elif s[i - 1] == " ":
            result = result + (s[i].upper())
        else:
            result = result + s[i]
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
