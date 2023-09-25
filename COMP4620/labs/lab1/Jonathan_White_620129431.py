import datetime
import math

#Question 1 (2)
def sum_z(num1, num2):
  return sum([num1, num2])


"""
Question 2 (2)
Write a function check_num that takes exactly one parameter param. The function should 
check if the param entered is an integer. If it is an integer the function should return 
True else return False.
Hint => You can use the function isinstance to check of the param is an integer.
"""

def check_num(num):
  return isinstance(num, int)

"""
Write a function sum_int_list that takes a list as a parameter. The function should 
sum all the integers in the list and return the sum. This function must make use of the 
check_num function.
"""
def sum_int_list(numList: list):
  return sum([eachNum for eachNum in numList if check_num(eachNum)])

"""
Question 4 (3)
Write a function future_date that takes three parameters year, month and day (which 
represents a date) and returns True if the date is in future and False otherwise. These 
calculations are done by capturing the current date. The code given below captures the current 
date where the variables current_year contains the value for present year, 
current_month contains the value for the present month and current_day contains the 
value for the present day. Use these variables to check if the input date is in future. 
"""

def future_date(day, month, year):
  date = datetime.datetime.now()
  today = (date.day, date.month, date.year)
  return (year, month, day) > today

"""
Typically, programming languages have primitive div (i.e. /) and mod (i.e. %) operators. 
Assume that these operators do not exist in python, and you have to write your own functions. 
div takes two integers as input and keeps on subtracting the second from the first until the 
first number becomes less than the second number. The function keeps a track of how many 
times the second number is subtracted from the first and returns that number as the answer. 
mod also takes two integers as input and keeps on subtracting the second from the first until 
the first number becomes less than the second number. When the first number becomes less 
than the second, the value of the first number is the answer
"""

def div(num1, num2):
  count = 0
  while num1 != num2 | num1 < num2:
    num1 -= num2
    count+=1
  return count

def mod(num1, num2):
  while num1 >= num2:
    num1 -= num2
  return num1


"""
Define a function isperfectSquare(n), which returns True if n is a perfect square and False otherwise. 

Your function takes a positive integer as input and returns a Boolean Value. 

Use while loops in writing this function. 

A number n is a perfect square if there is a number from 1 to n-1 whose square is equal to n.
"""

def isPerfectSquare(n: int):
  while True:  
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n
    

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True