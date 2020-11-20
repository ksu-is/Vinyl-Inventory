#vinyl color dictionary
#changed vinyl_stock to pantry_inventory
#changed contents of pantry_inventory
pantry_inventory = {"milk gallon": 10, "flour": 10, "egg carton": 10, "sugar": 5, "salt": 10, "coffee": 10, "broccoli": 10}

#User input which color vinyl they used
#changed this input function to accomodate my pantry_inventory
food = input ("What food item did you use? ")

#changed language here
def menu():
    print ("Press 1: To add to pantry. ")
    print ("Press 2: To check pantry. ")
    print ("Press 3: To enter a food item used. ")
    print ("Press q: To quit the program. ")
    return input ("What would you like to do? ")

run = menu()

#while true loop to run while entering vinyl stock
#changed to fit pantry_inventory syntax
while True:
    if run == "1":
        addStock = input ("What food item are you adding to the pantry? ")
        amount = int(input("How many of this item are you adding? "))
        #fixed issue in code where adding an item would not add it but instead replace it with amount added.
        pantry_inventory[addStock] += amount
        run = menu()
    
    elif run == "2":
        for key, value in pantry_inventory.items():
            print("{}: {}".format(key, value))
        run = menu()
    
    elif run == "3":
        if food in pantry_inventory:
            pantry_inventory[food] -= 1
            print (pantry_inventory)
            run = menu()
        else:
            print ("{} is out of stock".format(food))
            run = menu()
    elif run == "q":
        break

#print to end program        
print("The program has ended")


