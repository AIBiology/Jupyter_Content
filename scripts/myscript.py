#!/usr/bin/env python

# file: myscript.py
# Modified from Jake VanderPlas Python Data Science Handbook

def square(x):
    """square a number"""
    return x ** 2

for N in range(1, 4):
    print(f"{N} squared is {square(N)}")