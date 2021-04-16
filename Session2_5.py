# Session 2 Problem 05: Average of sequence

""" STATEMENT: Determine the average a of all elements of the sequence ending with the number 0.

Note.Print only the integer part of a(ignore fractional part).

For example, on input 1 2 4 0 output must be 2

TEMPLATE:

TESTS:
Input: 1 2 0 Output: 1
Input: 6 8 9 2 0 Output: 6
Input: 7 6 1 2 3 6 10 0 Output: 5 """

num = int(input("Type in the sequence numbers, type 0 when finished: "))
total = 0
count = 0

while num != 0:
    total += num
    count += 1
    num = int(input("Type in the sequence numbers, type 0 when finished: "))
a = int(total/count)
print(a)