#Input:  make sure to write down a variable for the kilos in the ten kilo race 
#make sure to write down a variable for the seconds completed in the race
# Also make sure to do a conversion variable for a kilometer to the mile 
# With that, make sure to divide variable one into the conversion variable to get the miles ran throughout the race 

# Then, make sure to divide the seconds ran by the miles run 
#Then, divide that again by 60 to get the rounded figure for the pace per mile. 

#Lets try to code this! 

secondsInHour = 3600
tenKilos = 10 
minutesCompleted = 42.42 
oneMile = 1
oneKilo = 1.61 

totalSecondsRun = (60 * 42) + 42 
totalMiles = tenKilos / oneKilo
totalDistance = totalSecondsRun / totalMiles 
averagePace = totalDistance / 60
averageTimeInMinute = averagePace // 1  
averageTimeOne = averagePace % 1
averageTimeTwo = averageTimeOne * .6
averageTimeInSeconds = averageTimeTwo * 100
averageTimeInSecond = round(averageTimeInSeconds, 2)
averageSpeedMile = secondsInHour / totalSecondsRun 
speedMph = averageSpeedMile * totalMiles 
averageSpeedMph = round(speedMph, 2)

print("Total seconds run is: ", totalSecondsRun)
print("Miles: ", totalMiles)
print(f"My average time per mile was: {averageTimeInMinute}m {averageTimeInSecond}s")
print("speed (mph):", averageSpeedMph)

