#print the characters inbetween the given input letter using function
def inbetween(first_index,last_index): #  function starts
    letter = input("enter the letter = ") # get the letter 
    for index in range(0,len(input1)): 
        if(input1[index] == letter): #if the input of the index is equal to the letter
            first_index = index # first index stores the index value  of the letter in a string
            break 
    for index in range(len(input1)-1,first_index,-1):
        if(input1[index] == letter): #if the input of the index is equal to the letter
            last_index = index # last index stores the index value  of the letter in a string
            break
    if(first_index == None or last_index == None): # if first or last index there is none it again calls the function
        print("there is no " + letter + " in the first  or last ")
        inbetween(first_index,last_index)
    else: # display the inbetween characters of the given letter
        for characters in range((first_index + 1),last_index):
            print(input1[characters],end=" ")
input1 = input("enter the string = ") # get the string 
first_index = None # set the first index as 'none'
last_index = None # set the last index as 'none'
inbetween(first_index,last_index) # call the function