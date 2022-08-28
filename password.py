print("password must contain altleast 8 characters including alphabets, numbers and special characters ")
print("                                                                                                ")
password = input("enter your password = ")
# for counting the characters
alphabets = 0
numbers = 0
special_characters = 0
for count in range(0,len(password)):
    if((password[count] >= 'A' and password[count] <= 'Z') or (password[count] >= 'a' and password[count] <= 'z')):
        alphabets += 1
    elif((password[count] >= '0' and password[count] <= '9')):
        numbers += 1
    else:
        special_characters += 1
#for checking your password 'strong' 
if((alphabets >= 3) and (numbers >= 1) and (special_characters >= 1) and (len(password)) >= 8):
    if(len(password) >= 16):
        print("very strong")
        print("acceptable")
    else:
        print("strong")
        print("acceptable")
#for checking your password 'ok'
elif((alphabets >=1) and (numbers >= 1) and (special_characters >= 1) and (len(password) >= 8)):
    print("ok !")
    print("acceptable")
# for checking the password 'weak'
elif(((alphabets == len(password)) or (numbers == len(password)) or (special_characters == len(password))) and len(password) >=8):
    print("weak !!")
    print("not acceptable")
else:
    print("password must contain altleast 8 characters including alphabets, numbers and special characters ")
    print("______________________________________________________________________________________________")
