#!/usr/bin/python3

def evens(n):
    result = (list(filter(lambda x: x % 2 == 0, range(n+1))))
    return result
