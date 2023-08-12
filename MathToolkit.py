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
    15: (standard_deviation, "Standard Deviation"),
    16: (None, "Exit")
}

# Function to get user input with data type validation
def get_user_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")
            
# Main function to handle user interaction
def main():
    while True:
        print("Available functions:")
        for func_num, (_, func_name) in FUNCTIONS.items():
            print(f"{func_num}. {func_name}")

        # Get user's choice for the function
        choice = get_user_input("Enter the number of the function you want to perform: ", int)

        if choice in FUNCTIONS:
            if choice == 16:
                print("Exiting the calculator.")
                break

            # Retrieve chosen function and its name
            function, function_name = FUNCTIONS[choice]


            # Based on the chosen function, gather required inputs and perform the calculation
            if choice in [1, 2, 3, 4]:
                a = get_user_input("Enter the first number: ", float)
                b = get_user_input("Enter the second number: ", float)
                try:
                    print(f"Result of {function_name}: {function(a, b)}")
                except ValueError as e:
                    print("Error:", str(e))

            elif choice == 5:
                a = get_user_input("Enter the first number: ", int)
                b = get_user_input("Enter the second number: ", int)
                print(f"Result of {function_name}: {function(a, b)}")

            elif choice in [6, 7]:
                a = get_user_input("Enter the first number: ", int)
                b = get_user_input("Enter the second number: ", int)
                print(f"Result of {function_name}: {bin(function(a, b))}")

            elif choice in [8, 9, 10, 11]:
                n = get_user_input("Enter the value of n: ", int)
                if choice in [10, 11]:
                    r = get_user_input("Enter the value of r: ", int)
                    try:
                        print(f"Result of {function_name}: {function(n, r)}")
                    except ValueError as e:
                        print("Error:", str(e))
                else:
                    try:
                        print(f"Result of {function_name}: {function(n)}")
                    except ValueError as e:
                        print("Error:", str(e))

            elif choice in [12, 13, 14, 15]:
                numbers = []
                while True:
                    num = get_user_input("Enter a number (or 'done' to finish): ", str)
                    if num.lower() == 'done':
                        break
                    numbers.append(float(num))
                try:
                    print(f"Result of {function_name}: {function(numbers)}")
                except ValueError as e:
                    print("Error:", str(e))

        else:
            print("Invalid choice. Please enter a valid function number.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
