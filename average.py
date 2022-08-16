number=int(input("enter the number = "))
count=0
sum=0
average=0
while(number>0):
    count+=1
    sum+=number
    number=int(input("enter the number = "))
average=sum/count
print(average)