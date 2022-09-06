items = ['tea','vadai','coffee','puffs','cake']  #get the items in a list 
cost = [10,10,15,20,40]  #get the costs for the items in a list
supply = [100,80,90,70,50] # get the supply for the items in a list
copied_supply = [100,80,90,70,50] # copy  the supply list in a new list for restocking purpose
reduced_supply = [] # store the 20% value value for the supply
items_sold = [0,0,0,0,0] # to get a new list for storing the number of sold items

for quantity in range(0,len(supply)): #to  calculate the 20% down value of the supply and store it to reduced supply list
    reduced_supply.append((supply[quantity]) - ((supply[quantity] // 10) * 2))
    
for menu in range(0,len(items)): # display the menu
    print(str(items[menu]) + " " + str(cost[menu]) + "rs " + str(supply[menu]))

answer = "no" # type 'no' that the vendor continues his sale 
amount = 0 
total_cost_for_customer = 0
total_cost_for_day = 0
restock_count = 0 #for counting the number of times supplies would be restocked

#function starts
def sales(items,cost,supply,total_cost_for_customer,total_cost_for_day,answer,reduced_supply,restock_count):
    while(answer == "no"):
        customer = input("enter customer name = ")
        print("customer " + customer + " arrivves")
        for buy in range(0,len(items)):  
            if(supply[buy] <= reduced_supply[buy]):#if supply goes down to 20% 
                restock_count += 1
                def restock(copied_supply): # function for restocking the supply 
                    supply[buy] = copied_supply[buy]
                restock(copied_supply) # call the function restocking 
            order = int(input("how many "+ str(items[buy]) + " you want ?"))
            amount = (cost[buy] * order) # calculate the cost of the item
            total_cost_for_customer += amount # store it to the total cost for the customer
            total_cost_for_day += amount # store it to the total cost for the day
            supply[buy] -= order # reduce the supply with the customer order 
            items_sold[buy] += order
        print("customer " + str(customer) + " buys for " + str(total_cost_for_customer) +" rs")
        total_cost_for_customer = 0
        amount = 0
        print("available stocks")
        
        for menu in range(0,len(supply)):
            print(items[menu]," ",supply[menu]," available") 
        answer = input("you want to end the sale = ") # type 'no' that the vendor continues his sale   
        
    for i in range(0,len(items_sold)): # display the total number of items sold in the day
        print(str(items_sold[i]) + " " + str(items[i]) + " sold", end=" ")
        print()
    print("sales for the day = ",total_cost_for_day," rs") # display the collection of the day 
    print("number of times restocked = ",restock_count) # display the number of times restocked for the day
# call the function
sales(items,cost,supply,total_cost_for_customer,total_cost_for_day,answer,reduced_supply,restock_count)    