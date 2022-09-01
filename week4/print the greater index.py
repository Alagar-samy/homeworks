a=[]
n = int(input("enter total number of elements you get = "))
for i in range(0,n):
    a.append(int(input()))
x=0
index=0
max=a[0]
for i in range(1,len(a)):
    if(a[i]>max):
        max=a[i]
        index=i
for i in range(0,n):
    if(i!=index):
        if((a[i]*2) <= max):
            x=1
        else:
            x=0
            break
if(x == 1):
    print(index)
else:
    print("-1")
