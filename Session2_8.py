# Session 2 Problem 08 Fibonacci Numbers

""" STATEMENT: Fibonocci numbers are defined as follows:
Zeroth Fibonacci number F(0) is equal 0
Second Fibonacci number F(1) is equal 1
Third Fibonacci number F(2) is equal F(0) + F(1) is equal 1
...
Nth Fibonacci number F(N) is equal F(N-1) + F(N-2)

Given a none negative integer N, print the N-th Fibonacci number F(N)

For example, on input 4 output must be 3

TEMPLATE:

TESTS:
Input: 2 Output: 1
Input: 3 Output: 2
Input: 5 Output: 5
Input: 20 Output: 6765 """

num = int(input("type a number: "))

fib_N_minus1 = 1
fib_N_minus2 = 0

for i in range(2, num+1):
    fib_N = fib_N_minus1 + fib_N_minus2
    fib_N_minus2 = fib_N_minus1     # order matters when assigning new values!
    fib_N_minus1 = fib_N            # shuffle along the 'lower' in the order first

print(fib_N)