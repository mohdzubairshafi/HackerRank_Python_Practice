# Problem: https://www.hackerrank.com/challenges/merge-the-tools/


def merge_the_tools(string, k):
    strlist = []
    count = 1
    substr = ""
    for i in range(len(string)):
        if count < k:
            if string[i] in substr:
                count += 1
            else:
                substr += string[i]
                count += 1
        elif count == k:
            if string[i] in substr:
                pass
            else:
                substr += string[i]
            strlist.append(substr)
            count = 1
            substr = ""
        else:
            strlist.append(substr)
            count = 1
            substr = ""
    print(*strlist, sep="\n")


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
