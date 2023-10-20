"""
Question 1 - Simple if Statement:
Write a Python program that takes an integer as input and prints "Even" if it's an even number and "Odd" if it's an odd number.
"""
numType = input("Give me a #: ")
if int(numType) // 2 != 0:
    print("Odd")
else:
    print("Even")

"""
Question 2 - if-else Statement:
Create a program that asks the user for their age and prints "You are a minor" if the age is less than 18, otherwise, it should print "You are an adult."
"""
userAge = input("Age: ")
if int(userAge) < 18:
    print("you are a minor")
else:
    print("You are an adult")

"""
Question 3 - Nested if Statements:
Write a program that checks if a number is positive, negative, or zero and prints an appropriate message.
"""
number = int(input("Number: "))
if number < 0:
    print("Negative")
elif number > 0:
    print("Positive")
else:
    print("Zero")


"""
Question 4 - if-elif-else Statement:
Create a program that asks the user to enter their exam score as an integer. Depending on the score, the program should print "A" for scores 90-100, "B" for 80-89, "C" for 70-79, "D" for 60-69, and "F" for scores below 60.
"""
examScore = int(input("Exam Score: "))
if examScore in range(90, 100):
    print("A")
elif examScore in range(80,89):
    print("B")
elif examScore in range(70,79):
    print("C")
elif examScore in range(60,69):
    print("D")
else:
    print("F")

"""
Question 5 - Multiple Conditions:
Write a program that checks if a user-entered year is a leap year.

A leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400.
"""
year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

"""
Question 6 - Logical Operators:
Create a program that checks if a user-entered number is between 10 and 50 (inclusive). Use logical operators (and or or) in your condition.
"""
userNumber = int(input("#: "))
if (userNumber >10 ) and (userNumber<=50):
    print("valid")

"""
Question 7 - if Statements with Strings:
Write a program that asks the user for their favorite programming language and prints a message based on their choice.

For example, if they enter "Python," it should print "Great choice!"
"""
languageChoice = input("Enter your fav programming language: ")
if "Python" in languageChoice:
    print("Great choice")
else:
    print("Not a great choice")

"""
Question 8 - Short-Circuiting:
Create a program that avoids division by zero. Ask the user for two numbers, and if the second number is zero, print "Cannot divide by zero."
Otherwise, perform the division and print the result.
"""
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
if num2 == 0:
    print("Can't provide by zero")
else:
    print(f"quotient: {num1/num2}")