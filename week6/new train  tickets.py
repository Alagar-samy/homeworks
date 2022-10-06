''' 2. Calculate the cost of train tickets. Single one way ticket from Madurai to Chennai (or vice versa) is Rs1000. 
Adding a return ticket will cost Rs750 extra.
Family of 4 or more gets 20% off. Senior rate is 50% off.'''


cost = 1000
return_cost = cost + 750
ages = []
price = 0 
senior_count = 0
senior_amount = 0
tickets = 0

#create a funtion that get the number of tickets from th user
def ticket():
    tickets = int(input("how many tickets you want = "))
    return tickets

# function that finds the number of seniors in a family
def senior(tickets, ages, senior_count):
    print("enter your ages one by one")
    for age in range(0,tickets):
        ages.append(int(input("enter age = ")))
    for age in range(0,len(ages)):
        if(ages[age] >= 57):
            senior_count += 1
    return senior_count

#function that finds the total pprice for the tickets
def amount(tickets, cost):
    price = (tickets * cost)
    return price

#function that gives 20% off from the total price when the tickets greater than or equal to four
def discount_price(price):
    price -= ((price // 10) * 2)
    return price

#function that gives the 50% off from the total price for the seniors  
def senior_dis(ages,price,cost): 
    for age in range(0, len(ages)):
        if(ages[age] >= 57):
            price -= (((cost // 10) * 5))
            
    return price


#the main function starts to find the cost of train tickets
def train_tickets(tickets, ages, senior_count,cost,return_cost,price,senior_amount):
    tickets = ticket() # calling the ticket funtion to get the number of tickets from the user
    print("tickets = ",tickets)
    senior_count = senior(tickets, ages, senior_count) # calling the senior function to get the number of senior members 
    choice = input("you want return tickets = ") # get the input from the user that user want return ticket or not
    if(choice == 'yes'): #if user choose the return ticket then the cost of tickets will change by return cost
        cost = return_cost
    
    price = amount(tickets,cost) #calling the function to calculate the total price for the tickets 
    if(tickets >= 4):  #if the family has more than or equal to 4 persons then they get 20% off from the total
        price = discount_price(price) # calling the function to get 20% off
    if(senior_count > 0): #senior count  greater than zero
        price = senior_dis(ages,price,cost) # calling the function to get senior discount
    print("tickets you buy for = " + str(price) + "rs")
    senior_count = 0
    senior_amount = 0
    ages = []
    cost = 1000
    seller_choice = input("you want to continue the ticket sales = ") 
    if(seller_choice == 'yes'):
        train_tickets(tickets, ages, senior_count,cost,return_cost,price,senior_amount)
         

# calling the train tickets function to finfd the cost of train tickets
train_tickets(tickets, ages, senior_count,cost,return_cost,price,senior_amount) 