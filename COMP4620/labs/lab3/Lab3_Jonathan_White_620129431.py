"""
Question 1
Write a recursive function max_el to find the maximum element in a list of integers.

>>> max_el([1,3,533,55,2])
533
>>> max_el([21,5,66,55,54])
66
"""

def max_el(lst):
    # Base case: if the list is empty, return negative infinity
    if not lst:
        return float('-inf')

    # Recursive case: compare the first element with the maximum of the rest
    rest_max = max_el(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max


"""
Question 2
Write a function strength_check that accepts a string as a parameter and keeps
prompting until they enter a strong password. A strong password contains at least 8
characters, including uppercase letters, lowercase letters, numbers, and special
characters. Use a while loop for input validation

>>> strength_check (“Password”)
Too weak, try again:
>>> strength_check(“Vp9tLv$VY*EfEb$H”)
Password Accepted
>>> strength_check(xe8wzxKxyRTvyeh6)
Password Accepted
"""

def strength_check(password: str):
    specialCharacters = [",", "+", "=", "_", "[", "]", "{", "}", "#", "@", "$", "%", "^", ";", "/", "<", ">", "?"]

    while True:
        eightCharacters = len(password) >= 8
        upperCase = any(eachCharacter.isupper() for eachCharacter in password)
        lowerCase = any(eachCharacter.islower() for eachCharacter in password)
        number = any(eachCharacter.isdigit() for eachCharacter in password)
        specialCharactersCheck = any(eachCharacter in specialCharacters for eachCharacter in password)

        if eightCharacters and upperCase and lowerCase and number and specialCharactersCheck:
            print("Password Accepted")
            return

        password = input("Too weak, try again: ")

"""
Using a for loop write a python function rev_int that takes an integer as a
parameter and reverses its digits. For example, if the input is 12345, the output should
be 54321.
>>> rev_int (1825)
5281
"""
def rev_int(number: int):
    numList = []
    reverseNumList = []
    # convert list to string to easy conversion
    for eachNum in str(number):
        numList.append(eachNum)
    
    # grab the length of the list
    listLength = len(numList)

    for eachNum in numList:
        reverseNumList.append(numList[listLength-1])
        listLength -= 1
    return reverseNumList

"""
Question 4
Using any iterative method that you prefer, write a function called palindrome that
accepts a string as a parameter and checks if that word entered is a palindrome
(reads the same backward as forward).
>>> palindrome (“Hope”)
No!
>>> palindrome (“Radar”)
Yes!
"""

def palindrome(word: str):
    characterList = []
    reverseCharacterList = []
    for eachCharacter in word.lower():
        characterList.append(eachCharacter)

    # grab the length of the list
    listLength = len(characterList)

    for eachNum in characterList:
        reverseCharacterList.append(characterList[listLength-1])
        listLength -= 1

    
    if characterList == reverseCharacterList:
        return "Yes!"
    else:
        return "No!"

"""
Question 5
Write the same function palindrome as in the previous question, but now, do it
recursively.
>>> palindrome (“Hope”)
No!
>>> palindrome (“Radar”)
Yes!
"""
def palindrome(word: str):
    def is_palindrome_recursive(characters, start, end):
        if start >= end:
            return "Yes!"

        if characters[start] != characters[end]:
            return "No!"

        return is_palindrome_recursive(characters, start + 1, end - 1)

    characters = [char.lower() for char in word]
    return is_palindrome_recursive(characters, 0, len(characters) - 1)
