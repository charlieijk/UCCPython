score1 = float(input("Exam mark #1?"))
score2 = float(input("Exam mark #2?"))
score3 = float(input("Exam mark #3?"))

average = (score1 + score2 + score3) / 3

print(" The average is " + "%0.2f"% average)

if average < 40: 
    print("You did not pass - oh dear!")

if average == 40: 
    print("You have passed! But you barely scraped by")

if average > 40: 
    print("You have passed, good luck!")