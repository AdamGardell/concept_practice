# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:26:03 2020

@author: AdamG
"""

# Recursion practice!
# I want to use recursion to find the factorial of a function
# I think once I do this following a youtube example I should be able to
# write a program to calculate the sum of the fibonacci sequence up to a given
# number
# Youtube example: https://www.youtube.com/watch?v=TqqQld6m6A0

def fact(n):
    
    if(n == 0):
        return 1
    
    return n * fact(n - 1)
    
    
result = fact(10)

print(result)

