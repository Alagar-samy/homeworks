input1 = input("enter the string = ")
print("odd index characters")
for index in range(0,len(input1)):
    if(index % 2 != 0):
        print(input1[index],end =" ")
print()
print("even index characters in reverse order")
for index in range(len(input1)-1,-1,-1):
    if(index % 2 ==0):
        print(input1[index],end =" ")
    