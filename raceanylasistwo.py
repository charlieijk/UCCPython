raceDistance = 5 
secondsInHour = 3600
seconds = (35 * 60) + 20
kilometers = 5 * 1.61 
racePace = seconds / kilometers
raceActualPace = racePace / 60
racePaceMinutes = int(raceActualPace)
racePaceSeconds = (raceActualPace - racePaceMinutes) * 60

speed = secondsInHour / seconds
#total_speed= speed * kilometers
total_speed = kilometers / (seconds / 3600)

# Print statements with formatting
print(f"Total seconds run is:  {seconds}")
print(f"Kilometers:  {kilometers:.5f}")
print(f"My average time per kilometer was: {racePaceMinutes:.0f}m {racePaceSeconds:.2f}s")
print(f"Speed (kph): {total_speed:.2f}")
