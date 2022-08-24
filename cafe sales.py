items=['cake','tea','coffee','puffs','samosa']
price=[50,10,15,20,10]
supply=[50,200,150,100,150]
order=0
total_price=0
total_price_of_day=0
print("menu")
for menu in range (0,len(items)):
    print(str(items[menu]) + " " + str(price[menu]) + "Rs " + str(supply[menu]) + " available")
    print()
for customer in range(0,2):
    print("customer " + str(customer+1) + "  arrives")
    for choice in range(0,len(items)):
        order =int(input("how many " + str(items[choice]) + " you want ="))
        total_price += (order * price[choice])
        supply[choice] -= order
    total_price_of_day += total_price
    print("customer " + str(customer+1) + " buys for " + str(total_price))
    total_price = 0
    for menu in range (0,len(items)):
        print(str(items[menu]) + " " + str(price[menu]) + "Rs " + str(supply[menu]) + " available")
        print()
print("total sales of the day ",total_price_of_day)
