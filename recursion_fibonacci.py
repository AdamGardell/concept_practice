# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:46:10 2020

@author: AdamG
"""

# Goal: Practice recursion by writing a recursive function to calculate the
# value of the fibonacci sequence up to a given number of entries


# Function to recursively calculate the entry of the Fibonacci sequence
# up to the given number of entries in the sequence n (indexed from 1).

# The first few elements of the fibonacci sequence are
# value:        0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# entry number: 0, 1, 2, 3, 4, 5, 6, 7, ...
# this generalizes to fib[n] = fib[n-1] + fib[n-2]

# fib(6) should return 8, for example

# in this case I have to use two base cases since I had to recursively call
# back two places instead of just one.
def fib(n):
    
    if(n == 0):
        return 0
    
    if(n == 1):
        return 1
    
    return(fib(n - 1) + fib(n - 2))
    
    
# Now I want to create a function to add up all of the values of the fibonacci
# sequence up to the given entry number
    
# in order to supress the if __debug__ dialogue, run the script in
# git bash with "python -O <filename.py>"
# "python" runs the script with python 3, -O is the option to set
# __debug__ false.
def fib_sum(n):
    
    fib_sum = 0
    
    # loop through each value up to n and 
    for i in range(n):    
        fib_sum += fib(i)
        
        # I want this to work like an ifdef in C
        if __debug__:
            print("fib(%d) = %d" %(i, fib(i)))
            print("fib_sum(%d) = %d\n" %(i, fib_sum))
            
    return fib_sum


result = fib_sum(7)

print(result)