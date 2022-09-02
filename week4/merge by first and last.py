#print 1st and last character ogf the string and add comma and so on
input1 = input("enter the 1st string = ")
output = ""
last_index = (len(input1) - 1)
for index in range(0, len(input1)):
    # index value is less than last index value if it is true it enters the if condition
    # else it breaks the loop
    if(index < last_index):
        output += input1[index] + input1[last_index] 
        #index + 1 not eqaul to the last index means to add comma else it equals means to add full stop
        if((index + 1) != last_index):
            output += ','
        else:
            output += '.'
        #decrement the last index value
        last_index -= 1
    else:
        break
print("output",output)

test case 1:

enter the 1st string = abcd1234
output a4,b3,c2,d1.

test case 2:
  
enter the 1st string = alagar123456
output a6,l5,a4,g3,a2,r1.
