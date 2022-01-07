#!/usr/bin/python3
""" Fx to count the minimun operations needed """

def minOperations(n):
    counter = 0
    temp = 0
    addition = 1

    if n < 2:
        return 0

    while addition < n:
        if n % addition == 0:
            temp = addition
            addition *= 2
            counter += 1
        else:
            addition += temp
        counter += 1
    return counter
 