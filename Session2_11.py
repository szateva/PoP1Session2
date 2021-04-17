# Session 2 Problem 11 Multiplication table

""" STATEMENT: Give two numbers N and M, print the multiplication table with N rows and M columns.
In the cell at the row i and column j print the value of i*j. The cells must be separated by space
horizontally.

Hint. Use nested loops.

For example, on input 5 3

output must be
1 2 3
2 4 6
3 6 9
4 8 12
5 10 15

TEMPLATE:

TESTS:
Input: 5 3
Output:
1 2 3
2 4 6
3 6 9
4 8 12
5 10 15

Input: 1 1
Output:
1

Input: 3 8
Output:
1 2 3 4 5 6 7 8
2 4 6 8 10 12 14 16
3 6 9 12 15 18 21 24

Input: 4 1
Output:
1
2
3
4

Input: 1 4
Output:
1 2 3 4 """

num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))

for first in range(1, num1+1):
    print()
    for second in range(1, num2+1):
        print(first * second, end=" ")