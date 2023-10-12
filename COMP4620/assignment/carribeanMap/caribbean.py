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
        
"""
        Task 6: [12 Marks]
        Option 1 - Create a new Disturbance is selected the program shall ask the user to enter the name of the next disturbance and shall use the makeDisturbance to create a new tropical disturbance.
        
        Option 2 - Run One Tick is selected The program shall update the position of each tropical disturbance (remember each disturbance travels westward) covering one column for every 5 miles per hour that it is travelling.
        
        Option 3 - Show All Disturbances is selected, the program shall display a listing of all active disturbances appropriately formatted.
        
        Option 4 - Show All Cities is selected, the program shall display a listing of all cities on the map appropriately formatted.

        Option 5 - Display Bulletins is selected, the program shall display a list of cities that are in the same cell (row and column) as a disturbance and issue a bulletin for the city. The bulletin shall give all the information about the disturbance
        
        Option 6 - Exit is selected, the program shall stop running.
"""

def displayDisturbance(disturbanceDict: dict) -> str:
    # checks if there is an entry in the dict
    if disturbanceDict:
        # iterates over ALL entries in the dict
        for eachDisturbance in disturbanceDict:
            # for each entry in the dict relevant information is printted (name, intensity etc.)
            print(f"\nDisturbance Name: {disturbanceDict[eachDisturbance]['Disturbance'][0]}\nDisturbance Intensity: {disturbanceDict[eachDisturbance]['Disturbance'][1]}\nDisturbance Travel Speed: {disturbanceDict[eachDisturbance]['Disturbance'][2]}\nDisturbance Coords: {disturbanceDict[eachDisturbance]['Coords']}\nTicks: {disturbanceDict[eachDisturbance]['Ticks']}")
    # if nothing is found within the dict then a message is printed to alert the user of the error throwm 
    else: print("ERROR CASE3: No Disturbances Found (Create a disturbance first)")

def gui():
    # Houses all the future disturbances to be created
    disturbanceDict = {}
    option = 0
    while True:
        option = int(input("\n1. Create a new disturbance\n2. Run One Tick\n3. Show All Disturbances\n4. Show All Cities\n5. Display Bulletins\n6. Exit\n\nSelect An option: "))
        match option:
            case 1:
                disturbance = makeDisturbance(input("\nDisturbance Name: "))
                # Append the new disturbance to the disturbanceDict dictionary
                disturbanceDict[disturbance[0]] = {
                    "Disturbance": disturbance,
                    "Coords": [disturbance[3], disturbance[4]],
                    "Ticks": disturbance[1] // 5
                    }
            case 2:
                # checks if there is an element inside of the dict
                if disturbanceDict: 
                    # Controls the movement of the disturbance
                    dx = rand.choice([-1, 0, 1])
                    dy = rand.choice([-1, 0, 1])
                    for eachDisturbance in disturbanceDict:
                        # checks the total amount of ticks within a disturbance
                        if disturbanceDict[eachDisturbance]['Ticks'] > 0:
                            # holds the coords from each disturbance 
                            cordsList = disturbanceDict[eachDisturbance]['Coords']
                            # Update the coordinates based on the random choices and ticks
                            updated_x = min(max(cordsList[0] + dx, 0), 13)
                            updated_y = min(max(cordsList[1] + dy, 0), 8)
                            # Update the disturbance with the new coord
                            disturbanceDict[eachDisturbance]['Coords'] = [updated_x, updated_y]
                            # Grabs the total ticks
                            totalTicks = disturbanceDict[eachDisturbance]["Ticks"]
                            # Remove a tick
                            disturbanceDict[eachDisturbance]["Ticks"] = totalTicks - 1
                        else:
                            # If ticks are 0 or less, remove the disturbance
                            print("Ticks Completed....Removing disturbance...")
                            disturbanceDict.pop(eachDisturbance)
                else: print("ERROR: Please use option #1 to create a disturbance")
            case 3:
                displayDisturbance(disturbanceDict=disturbanceDict)
            case 4:
                # this iterates over each key in the given dictionary
                for eachCity in tenCities.items():
                    print(f"\nCountry: {eachCity[0]} \nCity Name: {eachCity[1]['capitalCity']}\nRow Number: {eachCity[1]['rowNumber']} \nColumn Number: {eachCity[1]['colNumber']}\n")
            case 5:
                bulletin = [
                    displayDisturbance(disturbanceDict=eachDisturbance) for eachDisturbance in disturbanceDict
                    if disturbanceDict and any(
                        disturbanceDict[eachDisturbance]['Coords'] == [eachCity[1]['rowNumber'], eachCity[1]['colNumber']] for eachCity in tenCities.items()
                    )]
                if not bulletin:
                    print("No disturbances are in any countries.")
                else:
                    for item in bulletin:
                        print("DISTRUBANCE ALERT\n", item)
            case 6:
                exit()
            case _:
                print("ERROR: Incorrect number chosen. Please pick a number between 1 -> 6")
                
if __name__ == "__main__":
    gui()