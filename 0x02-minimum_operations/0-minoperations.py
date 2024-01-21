#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ minOperations """
    if n <= 1:
        return 0
    i = 2
    sum = 0
    while i <= n:
        if n % i == 0:
            sum += i
            n = n / i
        else:
            i += 1
    return sum
