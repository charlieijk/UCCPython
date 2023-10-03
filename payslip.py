hours_worked = int(input("How many hours do you work per week? "))


basic_rate = 12
basic_hours = 40
overtime_rate = 20

basic_pay = basic_rate * basic_hours
if hours_worked > basic_hours: 
    overtime_hours = hours_worked - basic_hours
    total_hours = hours_worked + overtime_hours
    ot_pay = overtime_rate * overtime_hours
    total_pay = basic_pay + ot_pay
else:
    basic_pay = basic_rate * hours_worked
    ot_pay = 0
    total_pay = basic_pay

print("The amount of hours that you have worked is " , hours_worked )
print("The basic pay that you have brought home is " , basic_pay)
print("The overtime pay that you have brought home is" , ot_pay)
print("The total pay that you have brought home is" , total_pay)
