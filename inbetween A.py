input1 = input("enter the letters = ")
start=0
end=0
for i in range(0,len(input1)):
    if(input1[i] == 'A'):
        start=i
        print("letter A  fisrt occurs in the index of  ",start)
        break
for i in range((len(input1) - 1),-1,-1):
    if(input1[i] == 'A'):
        end=i
        print("letter A  last occurs in the index of  ",end)
        break
print("letters inbetween the first and last A are")
for i in range((start+1),end):
    print(input1[i])