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
