# Session 2 Problem 04: Sum of sequence

""" STATEMENT: Determine the sum of all elements in the sequence, ending with the number 0.

For example, on input 1 2 3 0 output must be 6

TEMPLATE:

TESTS:
Input: 8 9 0 Output: 17
Input: 9 8 7 6 5 0 Output: 35
Input: 10 10 20 10 10 10 10 10 10 0 Output: 100"""

num = int(input("Type in the sequence numbers, type 0 when finished: "))
total = 0

while num != 0:
    total += num
    num = int(input("Type in the sequence numbers, type 0 when finished: "))

print(total)