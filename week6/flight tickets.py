'''ages = []
today_date = int(input("enter today's date = "))
sales = 'yes'
def flight_tickets(ages,today_date,sales):
    weekday_mrng_count = 0
    weekday_afn_count = 0
    weekday_evng_count = 0
    weekend_count = 0
    total_cost = 0
    while(sales == 'yes'):
        travel_date = int(input("enter the date you travel = "))
        total_persons = int(input("enter how many persons = "))
        senior_count = 0
        senior_cost = 0
        for age in range(0,total_persons):
            ages.append(int(input("enter your ages one by one = ")))
        for count in range(0,total_persons):
            if(ages[count] >= 55):
                senior_count += 1
        weekday_morning = 1
        weekday_afternoon = 2
        weekday_evening = 3
        weekend= 4
        
        print("----------------------------------------------------------------------")
        print("1. WEEKDAY MORNING - 3500rs")
        print("----------------------------------------------------------------------")
        print("2. WEEKDAY MORNING - 3500rs")
        print("----------------------------------------------------------------------")
        print("3. WEEKDAY EVENING - 3000rs")
        print("----------------------------------------------------------------------")
        print("4. WEEKEND - 5000rs")
        print("----------------------------------------------------------------------")
        print("senior ticket per head 10% off")
        print("----------------------------------------------------------------------")
        print("you bought for less than 2 weeks get 20% off")
        print("----------------------------------------------------------------------")
        print("enter '1' for choosing catogry 1 ")
        print("**************************************************************************")
        print("enter '2' for choosing catogry 2 ")
        print("**************************************************************************")
        print("enter '3' for choosing catogry 3 ")
        print("**************************************************************************")
        print("enter '4' for choosing catogry 4 ")
        print("**************************************************************************")
        want = int(input("enter want catogry you want = "))
        if(want == weekday_morning):
            cost = (total_persons - senior_count) * 3500
            for cost in range(0,senior_count):
                senior_cost += (3500 - (3500/10))
            cost += senior_cost
            weekday_mrng_count += 1
        elif(want == weekday_afternoon):
            cost = (total_persons - senior_count) * 3500
            for cost in range(0,senior_count):
                senior_cost += (3500 - (3500/10))
            cost += senior_cost
            weekday_afn_count += 1
        elif(want == weekday_evng_count):
            cost = (total_persons - senior_count) * 3000
            for cost in range(0,senior_count):
                senior_cost += (3000 - (3000/10))
            cost += senior_cost
            weekday_evng_count += 1
        elif(want == weekend):
            cost = (total_persons - senior_count) * 5000
            for cost in range(0,senior_count):
                senior_cost += (5000 - (5000/10))
            cost += senior_cost
            weekend_count += 1
        else:
            print("invalid input ")
        checking_date = travel_date - today_date
        if(checking_date <= 0):
            checking_date *= (-1)
        if(checking_date <= 14):
            cost = (cost - ((cost/10) * 2))
        print('you bought ticket for = ',cost)
        sales = input("enter 'yes' if you want to continue the ticket sales = ")
        ages = []
        total_cost += cost
    print("total cost of the day = " + str(total_cost) + 'rs')
    print("weekend tickets sold for a day = ",weekend_count)
flight_tickets(ages,today_date,sales)
'''
#print("\033[1;32m This text is Bright Green  \n")
n=1
if(n!=1):
    print("\33[1;32m",n)
else:
    print("\33[1;31m",n)