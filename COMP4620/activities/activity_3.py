"""
Question 1 - Function Definition:
Define a Python function called greet that takes a single parameter, name, and prints a greeting message using that name. Call the function with your name.
"""
def greet(name: str):
    print(f"Yo! Wah gwan..{name}")

greet("Jonathan")

"""
Question 2 - Multiple Parameters:

Create a function called calculate_area that calculates and returns the area of a rectangle given its length and width as parameters. 

Call the function with different length and width values.
"""
def calculate_area(length: float, width: float):
    return length * width
print("The area is: ", calculate_area(length=9, width=9))

"""
Question 3 - Return Statement:
Define a function called find_max that takes two parameters, num1 and num2, and returns the maximum of the two numbers. Call the function with various number pairs to
find and print the maximum.
"""
def find_max(num1, num2):
    return max(num1, num2)
print("The largest of the two numbers are: ", find_max(69, 96))

"""
Question 4 - Default Parameter Value:
Create a function called power that takes two parameters, base and exponent, and calculates the result of base raised to the power of exponent.
Set a default value of 2 for exponent.
Call the function with different bases.
"""
def power(base, exponent=2):
    return base ** exponent
print(power(3))

"""
Question 5 - Function Composition:
Create two functions, double and square, that take a single argument and return its double and square, respectively. 

Then, write a function apply_operations that takes a list of numbers and applies both double and square functions to each number,
returning the results.
"""
def double(number):
    return number * number

def square(number):
    return number ** number

def apply_operations(numList: list):
    doubledList = list(map(double, numList))

    squareList = list(map(square, numList))

    return f"The doubled list is: {doubledList} \nThe square list is: {squareList}"

print(apply_operations([1,2,3,4,5]))

"""
Question 6 - Variable Scope:

Define a function called add_numbers that takes two parameters, x and y, and returns their sum.

Try to print the variables x and y outside the function. What happens?
"""
def add_numbers(x,y):
    return sum(x,y)

# print(x, y) # doesn't work since the variable are within the scope of the function 