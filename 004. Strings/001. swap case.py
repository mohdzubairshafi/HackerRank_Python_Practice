# problem: https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    toggleString = ""
    for letter in s:
        if letter.islower():
            toggleString += letter.upper()
        elif letter.isupper():
            toggleString += letter.lower()
        else:
            toggleString += letter

    return toggleString


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
