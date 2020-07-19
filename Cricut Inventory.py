vinyl_stock = {"red": 10, "blue": 10, "black": 10, "yellow": 5, "white": 10, "purple": 10, "green": 10}

color = input ("What color did you use? ")

def menu():
    print ("Press 1: To add stock. ")
    print ("Press 2: To check stock. ")
    print ("Press 3: To enter color stock used. ")
    print ("Press q: To quit the program. ")
    return input ("What would you like to do? ")

run = menu()

while True:
    if run == "1":
        addStock = input ("What color are you adding to the stock? ")
        amount = int(input("How many roles are you adding? "))
        vinyl_stock[addStock] = amount
        run = menu()
    
    elif run == "2":
        for key, value in vinyl_stock.items():
            print("{}: {}".format(key, value))
        run = menu()
    
    elif run == "3":
        if color in vinyl_stock:
            vinyl_stock[color] -= 1
            print (vinyl_stock)
            run = menu()
        else:
            print ("{} is out of stock".format(color))
            run = menu()
    elif run == "q":
        break

print("The program has ended")


