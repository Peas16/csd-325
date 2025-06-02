# Paul Fralix, Assignment 2.2
# This script implements a simple calculator that adds two numbers.
# It prompts the user for two numbers, adds them, and prints the result.
# Simple Calculator

def add_numbers(a, b):
    return a + b

def main():
    print("Simple Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print("The result is:", result)

if __name__ == "__main__":
    main()