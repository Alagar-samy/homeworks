import random # to generate random numbers by import 'random' module
number = int(input("enter the divisble number that you want to genrate = "))
limit = int(input("enter the limit = "))
def random_number(number,limit): # defining a function to generate random numbers divisible by the given input number
    for i in range(1,limit+1): 
        num = random.randint(1,limit+1)
        if(num % number == 0): # to chech the random number is divisible by the given input number
            print(num,end=" ")
random_number(number,limit) # calling the function


test case 1:
   
enter the divisble number that you want to genrate = 5
enter the limit = 50
30 15 50 35 25 45 10 35

test case 2:
   
enter the divisble number that you want to genrate = 7
enter the limit = 100
70 98 49 42 84 7 49 56 7 98 21 56
