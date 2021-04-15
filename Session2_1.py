# Session 2 Problem 01: List of Squares

""" STATEMENT: For a given integer N, print all the squares of integer numbers where the square is
less than or equal to N, in ascending order.

For example, on input 10 output must be 1 4 9

TEMPLATE:

TESTS:
Input: 1 Output: 1
Input: 20 Output: 1 4 9 16
Input: 100 Output: 1 4 9 16 25 36 49 64 81 100
Input: 1000 Output: 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900 961 """

num = int(input("Type a number: "))

for i in range(1, num + 1):
    squre = i**2
    if squre <= num:
        print(squre, end=" ")