# problem: https://www.hackerrank.com/challenges/text-wrap/problem


def wrap(string, max_width):
    newString = ""
    count = 1
    for i in range(len(string)):
        if count == max_width:
            newString += string[i] + "\n"
            count = 1
        else:
            newString += string[i]
            count += 1
    return newString


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
