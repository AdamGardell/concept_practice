# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:46:10 2020

@author: AdamG
"""

# Goal: Practice recursion by writing a recursive function to calculate the
# value of the fibonacci sequence up to a given number of entries


# Function to recursively calculate the entry of the Fibonacci sequence
# up to the given number of entries in the sequence n (indexed from 0).

# The first few elements of the fibonacci sequence are
# value:        1, 1, 2, 3, 5, 8, 13, 21, ...
# entry number: 0, 1, 2, 3, 4, 5, 6, ...
# this generalizes to fib[n] = fib[n-1] + fib[n-2]

# fib(5) should return 8, for example

# in this case I have to use two base cases since I had to recursively call
# back two places instead of just one.
def fib(n):
    
    if(n == 0):
        return 1
    
    if(n == 1):
        return 1
    
    return(fib(n - 1) + fib(n - 2))


result = fib(10)

print(result)