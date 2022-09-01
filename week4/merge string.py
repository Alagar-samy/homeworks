# merge the string
input1 = input("enter the 1st string = ")
input2 = input("enter the 2nd string = ")
output = ""
for index in range(0,len(input1)):
    #merge the characters of two input strings one by one
    output += input1[index] + input2[index]
print("output ",output)