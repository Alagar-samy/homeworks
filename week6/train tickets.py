cost = 1000
age_list = []
answer = 'yes'
senior_age = 55
def train_tickets(cost,age_list,senior_age,answer):
    while(answer == 'yes'):
        persons = int(input("enter the total number of members = "))
        for age in range(0,persons):
            age_list.append(int(input("enter the age of person " + str(age+1) + " = ")))
        return_ticket = input("if you want to add return ticket enter 'yes' = ")
        if(return_ticket == 'yes'):
            cost = 1750
            senior_discount = cost/2
            count = 0
            ticket = (cost) * persons
            if(persons >= 4):
                ticket = (ticket -((ticket/10)*2))
            for age in range(0,len(age_list)):
                if(age_list[age] >= senior_age):
                    count += 1
            ticket -= (senior_discount * count)
        else:
            senior_discount = cost/2
            count = 0
            ticket = cost*persons 
            if(persons >= 4):
                ticket = (ticket -((ticket/10)*2))
            for age in range(0,len(age_list)):
                if(age_list[age] >= senior_age):
                    count+=1
            ticket -= (senior_discount * count)
        print("train ticket bill = ",ticket, "rs")
        answer = input("if you want to sale the tickets enter 'yes' = ")
train_tickets(cost,age_list,senior_age,answer)