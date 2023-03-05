# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_scores = student_marks[query_name]
    sum = 0
    for mark in student_scores:
        sum += mark
    avg = sum / len(student_scores)
    print("%.2f" % round(avg, 2))
