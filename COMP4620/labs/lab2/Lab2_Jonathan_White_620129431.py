"""
Question 1
Write a Python function called check_odd_even that takes an integer as a parameter and prints whether it's odd or even.
"""

def check_odd_even(num: int):
    return f"{num} is odd" if num % 2 == 1 else f"{num} is even" 

"""
Question 2
Write a function Ttype that takes the lengths of three sides of a triangle as parameters and classifies it as "Equilateral," "Isosceles," or "Scalene." The function should work as seen below, printing the appropriate result.
"""

def Ttype(side1, side2, side3):
    return "This is an equilateral triangle." if side1 == side2 == side3 else \
    "This is an isosceles triangle." if side1 == side2 else \
    "This is a scalene triangle."

"""
Write a function called Ticket_price accepts a user’s age and original ticket
price for a movie ticket booking system. 

Based on the user's age, determine the ticket price (child, adult, or senior). 

The function must return the cost of the ticket based on the age of
the user. 

The cost of a child’s ticket is two times less than the original price. 
The cost for the adult ticket is three times the original price.
The cost for a senior ticket is the original ticket price. 

A child is less than 18 years old.
a senior is 60 years or older.
an adult is between 18 and 59 years old.
"""

def Ticket_price(userAge: int, ticketPrice: float):
    match userAge:
        # Child
        case _ as age if age in range(0, 18):
            return ticketPrice / 2
        # Adult
        case _ as age if age in range(18,60):
            return ticketPrice * 3
        # Senior
        case _:
            return ticketPrice

"""
Write a function in python called Split_bill which will help a group of friends out for dinner determine their portion of the bill. 

The function should take the bill amount and number of friends and return each person’s contribution and a tip amount. 

The tip amount is 10% of the bill amount.
"""
def Split_bill(billAmount: float, friends: int):
    return ((billAmount + 0.10 * billAmount) / friends, 0.10 * billAmount)

"""
Python function called strange_sum that accepts five numbers as parameters
Checks which of the parameters is furthest away from the fifth parameter in value
Returns the sum of the fifth parameter and that number
"""
def strange_sum(num1, num2, num3, num4, num5):
    return num5 + min([num1, num2, num3, num4, num5])

