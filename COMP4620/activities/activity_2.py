"""
Question 1 - Variable Declaration and Conversion:
Declare a variable called initial_value with the value "42", and another variable
increment with the value 5. Perform the following operations:

1. Convert initial_value to an integer.
2. Convert increment to a string.
3. Add initial_value and increment and store the result in a
new variable.
4. Print the result.
"""

initial_value = "42"
increment = 5

# 1
initial_value = int(initial_value)
#2
increment = str(increment)
#3
newVar = initial_value + int(increment)
#4
print(newVar)


"""
Question 2 - Multiple Variable Swap:
Swap the values of three variables, a, b, and c, without using any temporary variables. For
example, if a has the value 1, b has 2, and c has 3, the result should be a=2, b=3, and
c=1.
"""
# initial assignment
a=1
b=2
c=3
# swap
c=a
b=c
a=b

"""
Question 3 - User Input and Validation:
Prompt the user to enter a number. Check if the input is a valid positive integer. If it is, store
it in a variable called user_num. If not, keep prompting until a valid input is provided.
"""
user_num = input("Enter a number: ")
while int(user_num) < 0:
    user_num = input("Re-Enter a number: ")

"""
Question 4 - Variable Types and Conversion:

Create a variable called temperature with a floating-point value. Convert it to an integer, then to a string. 

Print each version along with its data type.
"""

temperature = 3.14
temperature = int(round(temperature))
print("New Type: ", type(temperature))
temperature = str(temperature)
print(f"New Type:{type(temperature)}")

"""
Question 6 - String Formatting:
Create variables to store a person's name, age, and hometown. Use string formatting to
generate a sentence that introduces the person, e.g., "Hello, I'm [Name]. I'm [Age] years old,
and I'm from [Hometown]."

>>> Var1 = 2
>>> Var2 = 3
>>> print("Var1 is:",Var1,"and Var2 is:",Var2)
Var1 is: 2 and Var2 is: 3
"""

name = "Jon"
age = 23
hometown = "Kingston"
print(f"Hello, I'm {name}. I'm {age} and I'm from {hometown}")