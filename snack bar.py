#prices for the items
price_of_coffee=100
price_of_vadai=100
price_of_sandwich=200
price_of_coke=60
new_price_of_coffee=50
total=0
discount=0
sandwich=int(input("enter how many sandwich you want = "))
coffee=int(input("enter how many coffee you want = "))
coke=int(input("enter how many coke you want = "))
vadai=int(input("enter how many vadai you want = "))
if((sandwich>1) or (vadai>2)):
    total+=(sandwich*price_of_sandwich)+(coffee*new_price_of_coffee)+(coke*price_of_coke)+(vadai*price_of_vadai)
elif((sandwich==1) and (coke==1) and (coffee==1) and (vadai==1)):
    total+=(sandwich*price_of_sandwich)+(coffee*price_of_coffee)+(coke*price_of_coke)+(vadai*price_of_vadai)
    total=total-((total/10)*2)
else:
    total+=(sandwich*price_of_sandwich)+(coffee*price_of_coffee)+(coke*price_of_coke)+(vadai*price_of_vadai)
if(total>1000):
    discount=total-((total/10)*2)
    print("discounted total is ",discount)
else:
    print("total is ",total)
