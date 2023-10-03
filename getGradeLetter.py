gradePercentage = input("Please enter the grade percentage on your desired subject.")

if gradePercentage >= '85' and gradePercentage <= '100':
    print("Your grade is an 'A'")

elif gradePercentage >= '70' and gradePercentage <= '84':
    print("Your grade is an 'B'")

elif gradePercentage >= '55' and gradePercentage <= '69':
    print("Your grade is an 'C'")

elif gradePercentage >= '40' and gradePercentage <= '54':
    print("Your grade is an 'D'")

elif gradePercentage >= '25' and gradePercentage <= '39':
    print("Your grade is an 'E'")

elif gradePercentage >= '0' and gradePercentage <= '24':
    print("Your grade is an 'F'")
else: 
    print("'X'")