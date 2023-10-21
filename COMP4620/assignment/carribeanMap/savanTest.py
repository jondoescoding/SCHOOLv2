disturbanceDict = {}
# checks if there is an element inside of the dict
if disturbanceDict: 
                    # Controls the movement of the disturbance
                    for eachDisturbance in disturbanceDict:
                        # holds the coords from each disturbance
                        cordsList = disturbanceDict[eachDisturbance]['Coords']
                        # checks the total amount of ticks within a disturbance
                        if cordsList[0] > 0:  #disturbanceDict[eachDisturbance]['Ticks']
                            # Update the coordinates based on the random choices and ticks
                            movement = disturbanceDict[eachDisturbance]['Speed'] // 5
                            updated_x = cordsList[0] - movement #min(max(cordsList[0] + dx, 0), 13)
                            #updated_y = min(max(cordsList[1] + dy, 0), 8) 
                            # Update the disturbance with the new coord
                            disturbanceDict[eachDisturbance]['Coords'] = [updated_x,cordsList[1]]
                            # Grabs the total ticks
                            #totalTicks = disturbanceDict[eachDisturbance]["Ticks"] 
                            # Remove a tick
                            #disturbanceDict[eachDisturbance]["Ticks"] = totalTicks - 
                        else:
                            # If x coordinate equal to 0 remove the disturbance
                            print("Disturbance left region...Removing disturbance...")
                            disturbanceDict.pop(eachDisturbance)
                else: print("ERROR: No Disturbace Detected. Please use option #1 to create a disturbance")