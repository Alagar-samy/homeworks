#prices for the items
price_of_coffee=100
price_of_vadai=100
price_of_sandwich=200
price_of_coke=60
new_price_of_coffee=50
total=0
#display the menu in the snack bar
menu=[['items   ','quantity',' cost'],
      ['coffee  ','   1','   100.Rs'],
      ['vadai   ','   1','   100.Rs'],
      ['sandwich','   1','   200.Rs'],
      ['coke    ','   1','   60.Rs']]
for i in range(0,len(menu)):
    for j in range(0,len(menu[0])):
        print(menu[i][j],end=" ")
    print()
print("                  ***offers***")
print("(buy 1+ sandwich / 2+ vadai get coffee (1) just 50.Rs only)")
print("(buy atleast one in each items get 20% discount)")
print("(buy for more than 1000.Rs get 20% discount)")
#enter the items that customer wants
sandwich=int(input("enter how many sandwich you want = "))
coffee=int(input("enter how many coffee you want = "))
coke=int(input("enter how many coke you want = "))
vadai=int(input("enter how many vadai you want = "))
#cheching sandwich is greater than 1 or vadai is greater than 2
if((sandwich>1) or (vadai>2)):
    total+=(sandwich*price_of_sandwich)+(coffee*new_price_of_coffee)+(coke*price_of_coke)+(vadai*price_of_vadai)
#checking customer buys atleast one of the each item 
elif((sandwich>=1) and (coke>=1) and (coffee>=1) and (vadai>=1)):
    total+=(sandwich*price_of_sandwich)+(coffee*price_of_coffee)+(coke*price_of_coke)+(vadai*price_of_vadai)
    total=total-((total/10)*2)
else:
    total+=(sandwich*price_of_sandwich)+(coffee*price_of_coffee)+(coke*price_of_coke)+(vadai*price_of_vadai)
if(total>1000):
    total=total-((total/10)*2)
    print("discounted total is ",total)
else:
    print("total is ",total)
print("<<<thank you>>>")

output:
items    quantity  cost 
coffee      1     100.Rs 
vadai       1     100.Rs
sandwich    1     200.Rs
coke        1     60.Rs
                  ***offers***
(buy 1+ sandwich / 2+ vadai get coffee (1) just 50.Rs only)
(buy atleast one in each items get 20% discount)
(buy for more than 1000.Rs get 20% discount)
enter how many sandwich you want = 2
enter how many coffee you want = 10
enter how many coke you want = 0
enter how many vadai you want = 0
total is  900
<<<thank you>>>
