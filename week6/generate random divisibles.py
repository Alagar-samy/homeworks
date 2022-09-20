import random # to generate random numbers by import 'random' module
number = int(input("enter the divisble number that you want to generate = "))
limit = int(input("enter the limit = "))
def random_number(number,limit): # defining a function to generate random numbers divisible by the given input number
    for i in range(1,limit+1): 
        num = random.randint(1,limit+1)
        if(num % number == 0): # to chech the random number is divisible by the given input number
            print(num,end=" ")
random_number(number,limit) # calling the function