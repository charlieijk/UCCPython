breakfast = input("What would you like to have for breakfast today?")

cost = 0
bread_cost = 4.20
egg_cost = 1.97
pudding_cost = 2.10
# breakfast_list = [bread, egg, pudding]

if breakfast == "bread":
    cost = bread_cost

elif breakfast == "egg": 
    cost = egg_cost

elif breakfast == "pudding": 
    cost = pudding_cost

else: 
    breakfast = False
    
print("I want to have some", breakfast, "and it will cost", str(cost))

