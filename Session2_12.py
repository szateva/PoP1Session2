# Session 2 Problem 12 Function maximum of 3 Numbers

""" STATEMENT: Implement a function max_three(num1, num2, num3) that returns the maximal
of three numbers num1, num2, num3.

Note. You must use functions in this excercise. Do not change the name of the required function.

For example, the result of n = max_three(4,2,5) printNo must be 5

TEMPLATE:

def max_three(num1, num2, num3):

'''provide implementation below'''

n = max_three(4,2,5)

TESTS:
Case 1:
max_three(4,2,5) must be 5
Case2:
max_three(7,2,1) must be 7
Case 3:
max_three(8,12,11) must be 12
Case 4:
max_three(9,2,9) must be 9 """

def max_three(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    elif num3 > largest:
        largest = num3
    return largest

a = max_three(4,2,5)
print(a)
print("should be 5")
b = max_three(7,2,1)
print(b)
print("should be 7")
c = max_three(8,12,11)
print(c)
print("should be 12")
d = max_three(9,2,9)
print(d)
print("should be 9")