# Session 2 Problem 02: Least divisor

""" STATEMENT: Given an integer not less than 2. Print its smallest integer divisor greater than 1.

For example, on input 9 output must be 3

TEMPLATE:

TESTS:
Input: 3 Output: 3
Input: 4 Output: 2
Input: 49 Output: 7
Input: 179 Output: 179 """

num = int(input("Type a number: "))

for i in range(2, num+1):
    if num % i == 0:
        print(i)
        break