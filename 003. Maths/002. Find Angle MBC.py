"""
we Know that in a right-angled triangle the median drawn to the hypotenuse is half the hypotenuse in length.
so small Triangle will become isosceles triangle hence
angle MBC == angle MCB 
angle MCB = Tan(AB/BC)

Alternative: https://en.wikipedia.org/wiki/Thales%27s_theorem

"""

# importing math
import math

# taking input from user
AB, BC = int(input()), int(input())
degree = chr(176)
ans = round(math.degrees(math.atan(AB / BC)))
print(ans, degree, sep="")
