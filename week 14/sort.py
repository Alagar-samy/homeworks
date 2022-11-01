numbers = [5,7,1,9,5]
'''total_num = int(input("enter total numbers = "))
for num in range(0,total_num):
    numbers.append(int(input("enter number = ")))'''

print("before sorting : ", *numbers)

for index in range(0,len(numbers)):   
    for check in range(index + 1,len(numbers)):
        if(numbers[index] > numbers[check]):
            temp = numbers[index]
            numbers[index] = numbers[check]
            numbers[check] = temp
        print(numbers)
    print("************************************")
    print(numbers)
    print("************************************")
        
print("after sorting :  = ",*numbers,end = " ")