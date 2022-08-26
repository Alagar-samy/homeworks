items = ['mango','apple','orange','banana']
cost = [10,25,15,10]
supply = [100,90,80,150]
selled_apple_price = 0
selled_orange_price = 0
selled_banana_price = 0
selled_mango_price = 0
selled_price_day = 0
days = ['monday','tuesday','wednesday']
for day in range(0,len(days)):
    print(days[day]," starts")
    if(days[day] == 'monday'):
        for menu in range(0,len(items)):
            print(items[menu] , ' ' , supply[menu] , ' ' , cost[menu] , 'rs')
        for item in range(0,len(items)):
            if(items[item] == 'apple'):
                supply[item] //=2
                selled_apple_price = (supply[item]) * (cost[item])
            elif(items[item] == 'orange'):
                supply[item] //=2
                selled_orange_price = (supply[item]) * (cost[item])
            elif(items[item] == 'mango'):
                supply[item] -= 10
                selled_mango_price = 10 * (cost[item])
            elif(items[item] == 'banana'):
                supply[item] -= 10
                selled_banana_price = 10 * (cost[item])
        selled_price_day = (selled_apple_price) + (selled_orange_price) + (selled_mango_price) + (selled_banana_price)
        print("sales for monday ",selled_price_day,"rs")
        selled_price_day = 0
        selled_apple_price = 0
        selled_orange_price = 0
        selled_banana_price = 0
        selled_mango_price = 0
    elif(days[day] == 'tuesday'):
        for menu in range(0,len(items)):
            print(items[menu] , ' ' , supply[menu] , ' ' , cost[menu] , 'rs')
        for item in range(0,len(items)):
            if(items[item] == 'apple'):
                selled_apple_price += supply[item]
                supply[item] = 0
            elif(items[item] == 'orange'):
                selled_orange_price += (((supply[item] // 75)*100)  - (supply[item])) * (cost[item])
                supply[item] = ((supply[item] // 75)*100) - supply[item]
            elif(items[item] == 'mango'):
                selled_mango_price += (supply[item] - 30) * (cost[item])
                supply[item] = 30
            elif(items[item] == 'banana'):
                selled_banana_price += (supply[item] - 30) * (cost[item])
                supply[item] = 30
        selled_price_day = (selled_apple_price) + (selled_orange_price) + (selled_mango_price) + (selled_banana_price)
        print("sales for tuesday ",selled_price_day,'rs')
        selled_price_day = 0
        selled_apple_price = 0
        selled_orange_price = 0
        selled_banana_price = 0
        selled_mango_price = 0
    elif(days[day] == 'wednesday'):
        for menu in range(0,len(items)):
            print(items[menu] , ' ' , supply[menu] , ' ' , cost[menu] , 'rs')
        for item in range(0,len(items)):
            if(items[item] == 'orange'):
                selled_orange_price = supply[item] * cost[item]
                supply[item] = 0
            elif(items[item] == 'mango'):
                selled_mango_price = supply[item] * cost[item]
                supply[item] = 0
            elif(items[item] == 'banana'):
                selled_banana_price = supply[item] * cost[item]
                supply[item] = 0
        selled_price_day = (selled_apple_price) + (selled_orange_price) + (selled_mango_price) + (selled_banana_price)
        print("sales for wednesday ",selled_price_day,'rs')
        selled_price_day = 0
        selled_apple_price = 0
        selled_orange_price = 0
        selled_banana_price = 0
        selled_mango_price = 0
                
                
                
  