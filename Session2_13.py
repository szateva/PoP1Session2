# Session 2 Problem 13 Length of segment

""" STATEMENT: Write a function distance(x1,y1,x2,y2) to compute the distance between
the points (x1, y1) and (x2, y2).

Use the well-known formula (recall Pyhagorean theorem).

For computing the square root of a number N you can use the function math.sqrt() from the
Python math library imported in the first line of the program.

Note. It is mandatory to use functions for this exercise. Required function name cannot be changed.

For example, the output of d = distance(1,2,6,8)
print(d)
must be 7.810249675906654

TEMPLATE:

import math

''' provide your implementation '''

TESTS:
Case 1:
distance(1,2,6,8) must be around 7.81
Case 2:
distance(1,5,5,2) must be around 5.0 """

import math

def distance(x1, y1, x2, y2):
    x_dist = x2-x1
    y_dist = y2-y1
    dist = math.sqrt(x_dist**2 + y_dist**2)
    return dist

d1 = distance(1,2,6,8)
print(d1)
print("must be around 7.81")
d2 = distance(1,5,5,2)
print(d2)
print("must be around 5.0")
d3 = distance(5, 2, 3, 1)
print(d3)
print("must be around 2.23")
d4 = distance(4, -2, 7, 5)
print(d4)
print("must be around 7.61")