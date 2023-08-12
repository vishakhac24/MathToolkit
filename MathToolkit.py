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
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]  # Calculate the next Fibonacci number
        sequence.append(next_num)  # Add the next number to the sequence
    return sequence

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def mean(numbers):
    return sum(numbers) / len(numbers)

def mode(numbers):
    counter = Counter(numbers)
    max_count = counter.most_common(1)[0][1]
    return [num for num, count in counter.items() if count == max_count]

def variance(numbers):
    mean_value = mean(numbers)
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    return variance(numbers) ** 0.5

# Dictionary to map function numbers to functions and names
FUNCTIONS = {
    1: (add, "Addition"),
    2: (subtract, "Subtraction"),
    3: (multiply, "Multiplication"),
    4: (divide, "Division"),
    5: (bitwise_and, "Bitwise AND"),
    6: (bitwise_or, "Bitwise OR"),
    7: (bitwise_nor, "Bitwise NOR"),
    8: (factorial, "Factorial"),
    9: (fibonacci, "Fibonacci"),
    10: (permutation, "Permutation"),
    11: (combination, "Combination"),
    12: (mean, "Mean"),
    13: (mode, "Mode"),
    14: (variance, "Variance"),
    15: (standard_deviation, "Standard Deviation")
}
