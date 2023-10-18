x = 42
print(type(x))

y = ['apple', 'banana', 'cherry']
print(type(y))

"""
o Convert the string "123" to an integer.
o Convert the integer 42 to a float.
o Convert the float 3.14 to a string.
o Convert the boolean True to an integer.
"""
int("123")
float(42)
str(3.14)
int(True)

"""
Question 3 - String Concatenation:
Declare two variables, first_name and last_name, containing strings. Use string
concatenation to create a full name and print it.
"""
first_name = "Jon"
last_name = "White"
print(first_name + " " + last_name)

"""
Question 4 - Numeric Operations:
Create two variables, num1 and num2, with numeric values. Write Python code to perform
the following operations and print the results:

o Addition (num1 + num2)
o Subtraction (num1 - num2)
o Multiplication (num1 * num2)
o Division (num1 / num2)
o Integer Division (num1 // num2)
o Modulus (num1 % num2)
o Exponentiation (num1 ** num2)
"""
num1 = 2
num2 = 3
print(f"{num1 + num2}\n{num1-num2}\n{num1*num2}\n{num1/num2}\n{num1//num2}\n{num1%num2}\n{num1**num2}")

"""
Question 5 - Scope and Global Variables:
Write a Python program with the following structure:
1. Define a global variable global_var with an initial value.
2. Create a function that attempts to modify global_var. Explain whether the modification is successful.
3. Inside the function, declare a local variable with the same name as global_var.
Explain what happens
"""
global_var = 10
def modifyGlobal():
    # global_var += 1 # won't work since the global_var is outside of the function scope
    # print(f"Modification is a success:{global_var}")
    global_var = 9
    print(global_var)
modifyGlobal()

"""
Question 6 - Boolean Operations:
Declare two boolean variables, is_raining and is_sunny.
Write Python code that prints whether it's a good day based on the values of these variables.
"""
import random
is_raining = True
is_sunny = False
if is_raining:
    print("Not a good day")
else:
    print("Good day")

"""
Question 7 - Complex Type Conversion:
Given a string "123.45", write Python code to convert it to an integer, then to a float, and finally back to a string. 
Print each intermediate result and the final string.
"""
var = "123.45"
print(f"Integer: {int(var)}") # not possible