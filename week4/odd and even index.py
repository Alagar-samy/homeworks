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
   
test case 1:
    
enter the string = abcd
odd index characters
b d
even index characters in reverse order
c a

test case 2:
    
enter the string = alagar
odd index characters
l g r
even index characters in reverse order
a a a
