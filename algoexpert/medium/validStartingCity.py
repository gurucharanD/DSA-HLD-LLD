def validStartingCity(distances, fuel, mpg):
	for i in range(0,len(distances)):
		
		startingCity = i
		currentCity = i
		nextCity = currentCity + 1 if currentCity < len(distances)-1 else 0
		availableFuel = fuel[i]
		distance = distances[i]

		while canIreachNextCity(distance,availableFuel,mpg) :
			if nextCity == startingCity:
				return i
			
			currentCity = nextCity
			nextCity = currentCity + 1 if currentCity < len(distances)-1 else 0
			availableFuel = availableFuel - ( distance / mpg ) + fuel[currentCity]
			distance = distances[currentCity]
		
    return -1

def canIreachNextCity(distance,fuel,mpg):
	fuel = round(fuel,2)
	print("->",distance,fuel,mpg,fuel*mpg >= distance)
	return True if fuel*mpg >= distance else False


# optimal approach, is finding the city that we enter with
# minimum amount of gas available in the tank
# greedy approach
# we enter the first city with 0 miles and we keep track 
# of the smallest value possible 

def validStartingCity(distances, fuel, mpg):
	
	numberOfCities = len(distances)
	milesRemaining = 0
	
	indexOfStartingCityCandidate = 0
	milesRemainingAtStartingCityCandidate = 0
	
	for cityIndex in range(1,numberOfCities):
		milesRemaining = milesRemaining + fuel[cityIndex-1]*mpg - distances[cityIndex-1]
		if milesRemaining < milesRemainingAtStartingCityCandidate:
				indexOfStartingCityCandidate = cityIndex
				milesRemainingAtStartingCityCandidate = milesRemaining
			
    return indexOfStartingCityCandidate

