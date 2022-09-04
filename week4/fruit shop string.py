fruits = ['apples','oranges','bananas']
required = False
order = ""
quantity = ""
supply = ['one','two','three','four','five','six','seven','eight','nine']
for menu in range(0,len(fruits)):
    print('nine ',fruits[menu]," available")
answer = input("what do you want to buy = ")
answer = answer.split()
for buy in range(0,len(answer)):
    if(answer[buy] in fruits):
        order += answer[buy] + ' '
    if(answer[buy] in supply):
        quantity += answer[buy] + ' '
        required = True
if(required == False):
    quantity += input("how many you want = ")
    if(quantity not in supply):
        quantity = ""
        print("not available please enter below")
        quantity += input("how many you want = ")
order = order.split()
quantity = quantity.split()
print("customer ordered")
for i in range (0,len(quantity)):
    print(quantity[i],' ',order[i])