# merge the string
input1 = input("enter the 1st string = ")
input2 = input("enter the 2nd string = ")
output = ""
for index in range(0,len(input1)):
    #merge the characters of two input strings one by one
    output += input1[index] + input2[index]
print("output ",output)

test case 1:
enter the 1st string = abcd
enter the 2nd string = 1234
output  a1b2c3d4
 
test case 2:
enter the 1st string = alagar
enter the 2nd string = 123456
output  a1l2a3g4a5r6
