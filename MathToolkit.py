# math module for mathematical calculations and functions.
# counter from collections is used for counting occurrences of elements
import math 
from collections import Counter

# Function Definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def bitwise_nor(a, b):
    return ~(a | b)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.prod(range(1, n + 1))

def fibonacci(n):
    if n <= 0:
        raise ValueError("Fibonacci sequence is not defined for non-positive numbers.")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
