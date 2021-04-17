# Session 2 Problem 14 Concatenation of Strings

""" STATEMENT: Implement a function concat(s1, s2) concatenating the string s1 with s2
and adding a space inbetween.

For example, the result of s = concat("John", "Doe")
print(s)
must be John Doe

TEMPLATE:
'''provide implementation here'''

s = concat("John", "Doe")
print(s)

TESTS:
Case 1:
concat("John", "Doe") must be "John Doe"

Case 2:
concat("ABC", "DEF") must be "ABC DEF"

Case 3:
concat("xyz", " abc") must be "xyz abc" """

def concat(s1, s2):
    s = s1 + " " + s2
    return s
a = concat("John", "Doe")
print(a)
print("must be John Doe")
b = concat("ABC", "DEF")
print(b)
print("must be ABC DEF")
c = concat("xyz", " abc")
print(c)
print("must be xyz abc")