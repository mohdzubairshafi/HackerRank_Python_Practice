# Problem: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == "__main__":
    studentsList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentsList.append([name, score])

    sortedStudentMarks = sorted(set(_[1] for _ in studentsList))
    secondLowestScore = sorted(sortedStudentMarks)[1]
    secondLowestStudentNames = sorted(
        [_[0] for _ in studentsList if _[1] == secondLowestScore]
    )
    print(*secondLowestStudentNames, sep="\n")
