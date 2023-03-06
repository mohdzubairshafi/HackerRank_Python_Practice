# problem: https://www.hackerrank.com/challenges/matrix-script/problem

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
string = ""
decode_pattern = r"(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])"

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
    for j in range(n):
        string += matrix[j][i]

final_message = re.sub(decode_pattern, " ", string)
print(final_message)
