'''
input1=input("enter the string 1 = ")
input2=input("enter the string 2 = ")
new_input1 = set(input1)
new_input2 = set(input2)
print(str(new_input1.intersection(new_input2)))
'''
a= input("enter ")
b= input("enter ")
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(a[i] == b[j]):
            print(a[i])
            b[j] += " "