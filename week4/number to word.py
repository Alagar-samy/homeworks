#store the numbers with its name by using dictionary( it stores key with value)
a = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
num = []
number = int(input("enter the number = "))
# to separate the number into single digits usinf while loop
while(number > 0):
    remainder = number % 10
    #to store the remainder value in the 'num' list
    num.append(remainder)
    number = number//10
# to print the word by loop staring with the length of the 'num' list
for word in range((len(num)-1),-1,-1):
    print(a[num[word]],end=" ")
    
test case 1:
 
enter the number = 156
one five six

test case 2:
    
enter the number = 123
one two three
