import random as rand

"""
Task 1: [4 Marks]
Create a module named caribbean.py that includes the names of up to ten cities from the map along with their coordinates and any other data you may find useful in solving the problem. Your code should demonstrate an understanding of Python built-in data structures.
"""

tenCities = {
    "Jamaica": {
    "capitalCity": "Kingston",
    "rowNumber": 4,
    "colNumber": 4,
    },

    "Haiti":{
    "capitalCity": "Port-Au-Prince",
    "rowNumber": 4,
    "colNumber": 6,
    },

    "DR":{
    "capitalCity": "Santo Domingo",
    "rowNumber": 4,
    "colNumber": 7,
    },

    "Puerto Rico":{
    "capitalCity": "San Juan",
    "rowNumber": 4,
    "colNumber": 8,
    },

    "Cuba":{
    "capitalCity": "Havana",
    "rowNumber": 2,
    "colNumber": 2,
    },

    "Bahamas":{
    "capitalCity": "Nassau",
    "rowNumber": 1,
    "colNumber": 4,
    },

    "Costa Rica":{
    "capitalCity": "San Jose",
    "rowNumber": 8,
    "colNumber": 1,
    },

    "Panama":{
    "capitalCity": "Panama City",
    "rowNumber": 8,
    "colNumber": 3,
    },

    "Venezuela":{
    "capitalCity": "Caracas",
    "rowNumber": 8,
    "colNumber": 8,
    },

    "Trinidad_Tobago":{
    "capitalCity": "Port Of Spain",
    "rowNumber": 8,
    "colNumber": 8,
    },
}


"""
The function makeInitialIntensity that accepts no parameter and shall return 
a random value between 10 and 160 representing the intensity of a disturbance. 
"""
def makeInitialIntensity():
    return rand.randint(10,160)


"""
The function makeInitialSpeed that accepts no parameter and shall return a 
random value between 5 and 10 representing the speed in miles per hour at which the tropical disturbance is travelling.
"""
def makeInitialSpeed():
    return rand.randint(5,10)

"""
The function makeInitialRow that accepts no parameter and shall return a 
random number between 1 and 8 representing the row at which the disturbance starts
"""
def makeInitialRow():
    return rand.randint(1,8)


"""
Task 3: [5 Marks]
Implement a function named makeDisturbance that accepts the name of a disturbance as its only parameter and returns a tuple of the form: 
"""
def makeDisturbance(name):
    intensity = makeInitialIntensity()
    travel_speed = makeInitialSpeed()
    x_coordinate = 13
    y_coordinate = makeInitialRow()
    return (name, intensity, travel_speed, x_coordinate, y_coordinate)

"""
Task 4: [7 Marks]
Implement a function named sayDisturbance that accepts a disturbance as its parameter and returns a string appropriately formatted with information about a disturbance. 

You may decide what data is returned by this function. However, the string that is returned should include a description of the disturbance according to the following chart: 

• Intensity under 55 miles per hour is a Tropical Depression 
• Intensity of 74-95 miles per hour up to and including 70 miles per hour is a storm
• Intensity of 74-95 miles per hour is a category 1 hurricane 
• Intensity of 96-110 miles per hour is a category 2 hurricane 
• Intensity of 111-129 miles per hour is a category 3 hurricane 
• Intensity of 130-156 miles per hour is a category 4 hurricane 
• Intensity of 157 miles, or above is a category 5 hurricane
"""
def sayDisturbance(disturbance: tuple) -> str:
    """_summary_

    Args:
        disturbance (tuple): should accept ONLY tuples from the function makeDistrubance

    Returns:
        str: the relevant information of the disturbance
    """
    # At index location #1 should be the intensity of the disturbance 
    match disturbance[1]:
        # Intensity under 55 miles per hour is a Tropical Depression 
        case _ as intensity if intensity in range(0, 55):
            return "Intensity under 55 miles per hour is a Tropical Depression"
        case _ as intensity if intensity in range(55, 95):
            return "Intensity of 74-95 miles per hour up to and including 70 miles per hour is a storm"
        case _ as intensity if intensity in range(74, 95):
            return "Intensity of 74-95 miles per hour is a category 1 hurricane"
        case _ as intensity if intensity in range(96, 110):
            return "Intensity of 96-110 miles per hour is a category 2 hurricane"
        case _ as intensity if intensity in range(111, 129):
            return "Intensity of 111-129 miles per hour is a category 3 hurricane "
        case _ as intensity if intensity in range(130, 156):
            return "Intensity of 130-156 miles per hour is a category 4 hurricane"
        case _:
            return "Intensity of 157 miles, or above is a category 5 hurricane"
        
def gui():
    disturbanceList = []
    option = 0
    while True:
        option = int(input("1. Create a new disturbance\n2. Run One Tick\n3. Show All Disturbances\n4. Show All Cities\n5. Display Bulletins\n6. Exit\n\nSelect An option: "))
        match option:
            case 1:
                disturbance = input("\nDisturbance Name: ") 
                disturbanceList.append(makeDisturbance(disturbance))
            case 2:
                pass
            case 3:
                for eachDisturbance in disturbanceList:
                        print(f"Disturbance Name: {eachDisturbance[0]}\nDisturbance Intensity: {eachDisturbance[1]}\nDisturbance Travel Speed: {eachDisturbance[2]}\nDisturbance X Cord: {eachDisturbance[3]}\nDisturbance Y Cord: {eachDisturbance[4]}\n")
            case 0:
                exit()
            case _:
                print("ERROR")
if __name__ == "__main__":
    gui()