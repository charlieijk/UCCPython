secret_num = int(input("Please pick a number, any basic integer!"))

if secret_num % 3 == 0 and secret_num % 5 == 0: 
    print("FizzBuzz!")
elif secret_num % 3 == 0: 
    print("Fizz")
elif secret_num % 5 == 0: 
    print("Buzz")
else: 
    print(secret_num)