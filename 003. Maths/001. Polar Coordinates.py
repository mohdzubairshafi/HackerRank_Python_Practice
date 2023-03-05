# problem : https://www.hackerrank.com/challenges/polar-coordinates/problem

import math
import cmath

c = complex(input())
r = math.sqrt((c.real**2 + c.imag**2))
angle = cmath.phase(c)
print(r, angle, sep="\n")
