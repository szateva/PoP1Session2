# Session 2 Problem 07 Number of elements greater than previous one

""" STATEMENT: A sequence consists of integer numbers and ends with the number 0.
Determine how many elements of this sequence are greater than their neighbours above.

For example, on input 3 2 3 1 4 4 3 0 output must be 2

TEMPLATE:

TESTS:
Input: 1 2 3 4 0 Output: 3
Input: 5 3 4 3 4 2 1 5 0 Output: 3
Input: 5 10 4 4 4 7 8 8 9 10 0 Output: 5 """

num = int(input("Type in the sequence numbers, type 0 when finished: "))
count = 0
previous = num
while num != 0:
    num = int(input("Type in the sequence numbers, type 0 when finished: "))
    if previous < num:
        count +=1
    previous = num

print("final count: ", count)