"""
Question 1 
Write a Python list comprehension to create a list of squares of the first 10 positive integers.
"""
sqrList = [eachNum**2 for eachNum in range(0,10)]

"""
Question 2
Given a list of names and corresponding ages, create a dictionary where names are keys and ages are values. Example: `["Alice", "Bob"]` and `[25, 30]` should result in `{"Alice": 25, "Bob": 30}`.
"""
def convertToDic(nameList: list, ageList:list):
    namesAgeDict = {}
    for eachName in nameList:
        for eachAge in ageList:
            namesAgeDict.update({
                eachName: eachAge
            })
    return namesAgeDict

"""
Question 3
Create a tuple containing three items: your name, your age, and your city. Assign it to a variable and print the tuple
"""
personalInfo = ("Jonathan", 23, "Kingston")
print(personalInfo)

"""
Question 4
Write a Python function char_count that accepts a string as an argument and counts the frequency of each character in a given string and returns the result as a dictionary.
"""
def char_count(text: str):
    freqDict = {}
    for eachCharacter in text:
        if eachCharacter in freqDict:
            freqDict[eachCharacter] += 1
        else:
            freqDict[eachCharacter] = 1
    return freqDict

print(char_count("hello"))


"""
Question 5
Write a Python function reverse_words to reverse the order of words in a sentence using list comprehension. You can Split the sentence into words using space as the delimiter
"""
def reverse_words(sentence:str):
    wordList = [eachWord for eachWord in sentence.split(" ")]
    reverseNumList = [wordList[i] for i in range(len(wordList)-1, -1, -1)]
    return " ".join(reverseNumList)

print(reverse_words("Hello World"))

