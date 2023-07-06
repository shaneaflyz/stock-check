from tabnanny import check
#function to make orders 
def order():
    global bun, chicken_patty,  beef_patty, egg, burgerName, burgerCost, burgerCount, burgerSubtotal, total_price
    loop = True
    print("\nItems to order:")
    for n in range(len(burgerName)):
        print("{:.<2}{:27}RM{:.2f}".format(n+1,burgerName[n],burgerCost[n]))
    print()

    while loop:
        order_selection = int(input("Please select (1-8, 0 to end): "))
         #error checking
        while order_selection < 0 or order_selection > 8:
            order_selection = int(input("Error selecting. Please only select (1-8, 0 to end): "))

        #plain chicken
        if order_selection == 1:
            if bun < 1 or chicken_patty < 1:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                chicken_patty = chicken_patty-1
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1 
                total_price += burgerCost[order_selection-1]
        
        #chicken special
        elif order_selection == 2:
            if bun < 1 or chicken_patty < 1 or egg < 1:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                chicken_patty = chicken_patty-1
                egg = egg-1
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1 
                total_price += burgerCost[order_selection-1]

        #double chicken
        elif order_selection == 3:
            if bun < 1 or chicken_patty < 2:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                chicken_patty = chicken_patty-2
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1 
                total_price += burgerCost[order_selection-1]
        
        #double chicken special
        elif order_selection == 4:
            if bun < 1 or chicken_patty < 2 or egg < 1:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                chicken_patty = chicken_patty-2
                egg=egg-1
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1
                total_price += burgerCost[order_selection-1]
        
        #plain beef
        elif order_selection == 5:
            if bun < 1 or beef_patty < 1:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                beef_patty = beef_patty-1
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1 
                total_price += burgerCost[order_selection-1]
        
        #beef special
        elif order_selection == 6:
            if bun < 1 or beef_patty < 1 or egg < 1:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                beef_patty = beef_patty-1
                egg = egg-1
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1 
                total_price += burgerCost[order_selection-1]

        #double beef
        elif order_selection == 7:
            if bun < 1 or beef_patty < 2:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                beef_patty = beef_patty-2
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1 
                total_price += burgerCost[order_selection-1]

        #double beef special
        elif order_selection == 8:
            if bun < 1 or beef_patty < 2 or egg < 1:
                print("Sorry, out of stock.")
            else:
                bun = bun-1
                beef_patty = beef_patty-2
                egg = egg-1
                burgerSubtotal[order_selection-1] += burgerCost[order_selection-1]
                burgerCount[order_selection-1] = burgerCount[order_selection-1]+1
                total_price += burgerCost[order_selection-1]

        #exit
        elif order_selection == 0:
            print("RM{:.2f}".format(total_price))
            loop = False

#prints out receipt of the stock and material
def checkStock():
    gap = ' '*3
    print("Sales:")
    print("-"*58)
    print(f"{'Items':22}{gap}{'Quantity Sold':13}{gap}{'Subtotal':>16}")
    print("-"*58)
    for n in range(len(burgerName)):
        burgerData = f"{burgerName[n]:22}{gap}{burgerCount[n]:^13}{gap}{burgerSubtotal[n]:>16.2f}"
        print(burgerData)
    print("-"*58)
    print(f"{'Total'}{total_price:>52.2f}")
    print("="*58)

    print("\nRaw Material Left:")
    print("-"*25)
    print(f"{'Material':17}{gap}{'Qty.':4}")
    print("-"*25)
    print(f"{'Bun':17}{gap}{bun:^4}")
    print(f"{'Chicken Patty':17}{gap}{chicken_patty:^4}")
    print(f"{'Beef Patty':17}{gap}{beef_patty:^4}")
    print(f"{'Egg':17}{gap}{egg:^4}")
    print("="*25)

#variable declaration
burgerName = ["plain chicken", "chicken special", "double chicken", "double chicken special", "plain beef", "beef special", "double beef", "double beef special"]
burgerCost = [4.0, 5.0, 6.5, 7.5, 4.5, 5.5, 7.0, 8.5]
burgerSubtotal = [0,0,0,0,0,0,0,0]
burgerCount = [0,0,0,0,0,0,0,0]
total_price = 0

#ask to input the materials
print("Please input the amount for: ")
bun = int(input("Bun: "))
while bun < 1:
    bun = int(input("Please input value more than 1, Bun: "))
chicken_patty = int(input("Chicken Patty: "))
while chicken_patty < 1:
    chicken_patty = int(input("Please input value more than 1, Chicken Patty: "))
beef_patty = int(input("Beef Patty: "))
while beef_patty < 1:
    beef_patty = int(input("Please input value more than 1, Beef Patty: "))
egg = int(input("Egg: "))
while egg < 1:
    egg = int(input("Please input value more than 1, Egg: "))

#menu
while True:
    print("\nMenu:\n1.Order\n2.Check sales and stock\n3.End the day")
    selection = int(input("Please select an option: "))
    while selection > 3 or selection < 1 :
        print("Error please choose a correct option.")
        selection = int(input("Please select an option: "))
    #order
    if(selection == 1):
        order()

    #check sales
    elif(selection == 2):
        checkStock()

    #end the day
    elif(selection == 3):
        print("Thank you for using the system")
        break