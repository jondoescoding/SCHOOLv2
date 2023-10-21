import random as rand

"""
X = COLUMN
Y = ROW
"""

"""
Task 1: [4 Marks]
Create a module named caribbean.py that includes the names of up to ten cities from the map along with their coordinates and any other data you may find useful in solving the problem. Your code should demonstrate an understanding of Python built-in data structures.
"""

# Holds the inital list of ten cities which can be amended
tenCities = {
    "Jamaica": {
    "capitalCity": "Kingston",
    "x_coord": 13,
    "y_coord": 1,
    },

    "Haiti":{
    "capitalCity": "Port-Au-Prince",
    "x_coord": 13,
    "y_coord": 2,
    },

    "DR":{
    "capitalCity": "Santo Domingo",
    "x_coord": 13,
    "y_coord": 3,
    },

    "Puerto Rico":{
    "capitalCity": "San Juan",
    "x_coord": 13,
    "y_coord": 4,
    },

    "Cuba":{
    "capitalCity": "Havana",
    "x_coord": 13,
    "y_coord": 5,
    },

    "Bahamas":{
    "capitalCity": "Nassau",
    "x_coord": 13,
    "y_coord": 5,
    },

    "Costa Rica":{
    "capitalCity": "San Jose",
    "x_coord": 13,
    "y_coord": 6,
    },

    "Panama":{
    "capitalCity": "Panama City",
    "x_coord": 13,
    "y_coord": 7,
    },

    "Venezuela":{
    "capitalCity": "Caracas",
    "x_coord": 13,
    "y_coord": 1,
    },

    "Trinidad_Tobago":{
    "capitalCity": "Port Of Spain",
    "x_coord": 13,
    "y_coord": 3,
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
    """
    Outputs a number which is between 5 & 10
    """
    return rand.randint(5,10)

"""
The function makeInitialRow that accepts no parameter and shall return a random number between 1 and 8 representing the row at which the disturbance starts
"""
def makeInitialRow():
    """
    Outputs a random number between 1 and 8
    """
    return rand.randint(1,8)


"""
Task 3: [5 Marks]
Implement a function named makeDisturbance that accepts the name of a disturbance as its only parameter and returns a tuple of the form: 
"""
def makeDisturbance(name):
    """
    Generates a tuple which houses the:
    name, intensity, travel_speed, x coords and y coords of a disturbance
    """
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
    """Calls out the disturbance

    Args:
        disturbance (tuple): should accept ONLY tuples from the function makeDistrubance

    Returns:
        str: the relevant information of the disturbance
    """
    # At index location #1 should be the intensity of the disturbance 
    match disturbance[1]:
        # Intensity under 55 miles per hour is a Tropical Depression 
        case _ as intensity if intensity in range(0, 55):
            return f"Tropical disturbance {disturbance[0]} has an intensity below 55 miles per hour and classifies as a Tropical Drepression"
        case _ as intensity if intensity in range(55, 74):
            return f"Tropical disturbance {disturbance[0]} has an intensity 55-73 miles per hour and classifies as a Storm"
        case _ as intensity if intensity in range(74, 96):
            return f"Tropical disturbance {disturbance[0]} has an intensity between 74-95 miles per hour and classifies as a Category 1 hurricane" 
        case _ as intensity if intensity in range(96, 111):
            return f"Tropical disturbance {disturbance[0]} has an intensity between 96-110 miles per hour and classifies as a Category 2 hurricane" 
        case _ as intensity if intensity in range(111, 130):
            return f"Tropical disturbance {disturbance[0]} has an intensity between 111-129 miles per hour and classifies as a Category 3 hurricane"
        case _ as intensity if intensity in range(130, 157):
            return f"Tropical disturbance {disturbance[0]} has an intensity between 130-156 miles per hour and classifies as a Category 4 hurricane"
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

def makeCities():
    """Create a new city

    Returns:
        _type_: returns a dict containing the data on a new city
    """
    cityName = input("Enter City Name: ")
    capitalCity = input("Enter Capital City: ")
    x_coordinate = input("Enter x coordinate: ")
    y_coordinate = input("Enter y coordinate: ")
    city_info = {
        "capitalCity": capitalCity,
        "x_coord": x_coordinate,
        "y_coord": y_coordinate
    }

    # Create the outer dictionary and return it
    cityDict = {
        cityName: city_info
    }
    return cityDict

def gui():
    # Houses all the future disturbances to be created
    disturbanceDict = {}
    # which option the user will select
    option = 0
    while True:
        option = int(input("\n0. Create A City \n1. Create a new disturbance\n2. Run One Tick\n3. Show All Disturbances\n4. Show All Cities\n5. Display Bulletins\n6. Exit\n\nSelect An option: "))
        match option:
            # creates a new city
            case 0:
                newCity = makeCities()
                tenCities.update(newCity)
            # creates a new disturbance
            case 1:
                disturbance = makeDisturbance(input("\nDisturbance Name: "))
                # Append the new disturbance to the disturbanceDict dictionary
                disturbanceDict[disturbance[0]] = {
                    "Disturbance": disturbance,
                    "Coords": [disturbance[3], disturbance[4]], # [x = column, y = row]
                    "Ticks": disturbance[2] // 5,
                    "Off-Canvas": False # this is this to handle if the disturbance comes off the canvas 
                    }
                print("A disturbance was created!\n")
            # runs the simulation
            case 2:
                if disturbanceDict:
                    # Controls the movement of the disturbance
                    for eachDisturbance in disturbanceDict:
                        cordsList = disturbanceDict[eachDisturbance]['Coords']
                        if cordsList[0] > 0:
                            # Update the coordinates based on the random choices and ticks
                            movement = disturbanceDict[eachDisturbance]['Disturbance'][2] // 5
                            updated_x = cordsList[0] - movement
                            disturbanceDict[eachDisturbance]['Coords'] = [updated_x,cordsList[1]]
                        else:
                            # If the disturbance has left the caribbean map canvas
                            print("Disturbance left region...Removing disturbance...")
                            disturbanceDict[eachDisturbance]['Off-Canvas'] = True
                            
                else: 
                    print("ERROR: No Disturbace Detected. Please use option #1 to create a disturbance")
            # prints ALL of the disturnances in the dictionary
            case 3:
                # checks if there is an entry in the dict
                if disturbanceDict:
                    # iterates over ALL entries in the dict
                    for eachDisturbance in disturbanceDict:
                        # for each entry in the dict relevant information is printted (name, intensity etc.)
                        print(f"\nDisturbance Name: {disturbanceDict[eachDisturbance]['Disturbance'][0]}\nDisturbance Intensity: {disturbanceDict[eachDisturbance]['Disturbance'][1]}\nDisturbance Travel Speed: {disturbanceDict[eachDisturbance]['Disturbance'][2]}\nDisturbance Coords: {disturbanceDict[eachDisturbance]['Coords']}\nTicks: {disturbanceDict[eachDisturbance]['Ticks']}")
                        # if nothing is found within the dict then a message is printed to alert the user of the error throwm 
                else: 
                    print("ERROR CASE3: No Disturbances Found (Create a disturbance first)")
            # prints all of the cities
            case 4:
                # this iterates over each key in the given dictionary
                for eachCity in tenCities.items():
                    print(f"\nCountry: {eachCity[0]} \nCity Name: {eachCity[1]['capitalCity']}\nRow Number: {eachCity[1]['y_coord']} \nColumn Number: {eachCity[1]['x_coord']}\n")
            # displays a bulletin for each disturbance
            case 5:
                if disturbance:
                    for eachDisturbance in disturbanceDict:
                        for eachCity in tenCities:
                            if disturbanceDict[eachDisturbance]['Coords'] == [tenCities[eachCity]['x_coord'], tenCities[eachCity]['y_coord']]:
                                display = disturbanceDict[eachDisturbance]['Disturbance']
                                # Diturbance Information
                                print(f"\nDISTURBANCE ALERT\n{sayDisturbance(display)} \n--GENERAL INFORMATION--\nDisturbance Name: {display[0]} \nDisturbance Intensity: {display[1]} \nDisturbance Travel Speed: {display[2]} \nDisturbance X Coord: {display[3]} \nDisturbance Y Coord: {display[4]}")
            # exits the program
            case 6:
                exit()
            # captures if the user enters a wrong number
            case _:
                print("ERROR: Incorrect number chosen. Please pick a number between 1 -> 6")
                
if __name__ == "__main__":
    gui()
