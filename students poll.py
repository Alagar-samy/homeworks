students=10
female_count=0
online_count=0
percentage=0
for i in range(1,students+1):
    name=input("enter the name : ")
    gender=input("enter gender : ")
    opinion=int(input("enter <1> for online class / enter <2> for in preson class / enter <3> for both / enter <4> for no comments"))
    if(gender=='female'):
        female_count+=1
    if(opinion==4):
        break
    if(gender=='female' and opinion==1):
        online_count+=1
print("poll ends")
print("total female students",female_count,"online count",online_count)
percentage=(online_count/female_count)*100 
print(percentage,"percentage of females chosen online class")