# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:46:10 2020

@author: AdamG
"""

from datetime import datetime

# Goal: Practice recursion by writing a recursive function to calculate the
# value of the fibonacci sequence up to a given number of entries

test_num = 35


# Function to recursively calculate the entry of the Fibonacci sequence
# up to the given number of entries in the sequence n (indexed from 1).

# The first few elements of the fibonacci sequence are
# value:        1, 1, 2, 3, 5, 8, 13, 21, ...
# entry number: 0, 1, 2, 3, 4, 5,  6,  7, ...
# this generalizes to fib[n] = fib[n-1] + fib[n-2]

# fib(6) should return 13, for example

def fib_recursive(n):
    
    if(n == 0):
        return 1
    
    if(n == 1):
        return 1
    
    return(fib_recursive(n - 1) + fib_recursive(n - 2))
    
    
# Function to generate a list of the first n entries of the fibonacci
# sequence.
    
# The sequence is: 1, 1, 2, 3, 5, 8, 13, 21
    
def fib_list(n):
    
    fib_list = [1, 1]
    
    if (n == 0):
        fib_list = []
    elif (n == 1):
        fib_list = [1]
    elif (n == 2):
        fib_list = [1, 1]
    else:
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            
            if __debug__:
                print("Debug from fib_list()")
                print("n = %d, i = %d\n" %(n, i))
    
    return fib_list


# Function to add up all of the values of the fibonacci
# sequence up to the given entry number.
# Method: use the fib() function
    
# in order to supress the if __debug__ dialogue, run the script in
# git bash with "python -O <filename.py>"
# "python" runs the script with python 3, -O is the option to set
# __debug__ false.
    
# I think there must be a more efficient way of doing this. Right now the
# fib() function is called a bunch of times, so at every n all of the 
# processing from the previous n is done plus one more calculation.
# I think it would be more efficient to call the fib function once and save
# the fibonacci sequence into an array and then sum the elements of the array
    
def fib_sum_if(n):
    
    fib_sum = 0
    
    # loop through each value up to n
    for i in range(n):    
        fib_sum += fib_recursive(i)
        
        # Debug print statements. Run in git bash with python -O <filename>
        # to set __debug__ false and exclude these prints.
        if __debug__:
            print("Debug from fib_sum_if()")
            print("fib(%d) = %d" %(i, fib_recursive(i)))
            print("fib_sum(%d) = %d\n" %(i, fib_sum))
            
    return fib_sum


# Function to add up all of the values of the fibonacci sequence
# up to a given entry number.
# Method: use the fib_list() function rather than the fib() function 
    
def fib_sum_list(n):
    
    fib_sum = 0
    fib_sequence = []
    if __debug__:
        debug_print_count = 0
    
    # call fib_list(n) to get the list containing the fibonacci sequence
    fib_sequence = fib_list(n)
    
    # sum up the elements of the list, save to fib_sum
    for num in fib_sequence:
        fib_sum += num
        
        if __debug__:
            debug_print_count += 1
            print("Debug from fib_sum_list()")
            print("Sum up to and including value %d is %d" %(num, fib_sum))
            print("Debug print count = %d\n" %(debug_print_count))
            
    if __debug__:
        print(fib_sequence)
    
    return fib_sum



#result = fib_sum_if(test_num)
#print("RESULT1: %d" %(result))
#result = fib_sum_list(test_num)
#print("RESULT2: %d" %(result))

# find runtime of the recursive method
start_time_1 = datetime.now()
result_1 = fib_sum_if(test_num)
time_method_1 = datetime.now() - start_time_1



# find runtime of the list method
start_time_2 = datetime.now()
result_2 = fib_sum_list(test_num)
time_method_2 = datetime.now() - start_time_2


print("The runtime of the recursive method is ", time_method_1)
print("The runtime of the list method is ", time_method_2)