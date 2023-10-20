"""
Question 1 - while Loop Basics:
Write a while loop that prints numbers from 1 to 5.
"""

def q1():
    n = 0
    while (n := n + 1) < 5:
        print(n)
print(q1())

"""
Question 2 - for Loop Basics:
Write a for loop that prints even numbers from in this list: [2,3,4,5,6,7,8,9]
"""
def q2():
    numList = [2,3,4,5,6,7,8,9]
    for eachNum in numList:
        if eachNum % 2 == 0:
            print(eachNum)
print(q2())

"""
Question 3 - while Loop with User Input:
Create a program that asks the user to enter a positive integer. Use a while loop to print all the numbers from 1 to that integer.
"""
def q3():
    count = 0
    val = int(input("enter a positive integer: "))
    while (count := count + 1 ) < val:
        print(count)
#print(q3())

"""
Question 4 - for Loop with Lists:
Given a list of fruits: fruits = ["apple", "banana", "cherry"], use a
for loop to print each fruit.
"""
def q4():
    fList = ["apple", "banana", "cherry"]
    for eachFruit in fList:
        print(eachFruit)
print(q4())


"""
Question 5 - Sum of while Loop
Write a while loop that calculates the sum of all numbers from 1 to 100.
"""
def q5():
    num = 0
    total = 0
    while (num := num + 1) < 101:
        total += num
    print(total)
print(q5())

"""
Question 6 - for Loop with Range
Use a for loop to print all numbers from 10 to 1 (in reverse order).
"""
def q6():
    for eachNum in range(10, 0, -1):
        print(eachNum)
print(q6())

"""
Question 7 - while Loop with Conditional Break
Write a while loop that asks the user to guess a secret number (e.g., 7). Continue asking until the user guesses correctly.
"""
def q7():
    secretNum = 7
    while int((guess := input("Guess a number between 1-10: "))) != secretNum:
        print("Try Again!")
    print("Correct")
print(q7())