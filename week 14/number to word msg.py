'''You have a message that you want to send to your friend. You don't want others to see the message.
You code the message and send it.The alg to code is - split each word in half and reverse it 
(eg cricket becomes ketccri), if the word ends with a vowel, split at the 
last letter and reverse (eg cinema becomes acinem), if the word has numbers, spell the number but 
add A as first and last letters
(8 pm becomes AeightA pm ).
Write an app that can code and decode the message.'''

from num2words import num2words

message = input("enter the msg = ")
vowels = ['a', 'e', 'i', 'o', 'u','A', 'E','I','O','U']
output = ""
number = ""
answer = message.isalpha()
if(answer == True):
    if(message[-1] in vowels):
        output += message[-1]
        for change in range(0,len(message)-1):
            output += message[change]
    else:
        centre = len(message) // 2
        if(len(message) % 2 == 0):
            for last in range(centre,len(message)):
                output += message[last]
            for first in range(0,centre):
                output += message[first]
        else:
            for last in range(centre + 1,len(message)):
                output += message[last]
            output += message[centre]    
            for first in range(0,centre):
                output += message[first]
                
    print(output)
else:
    message = message.split()
    for num in range(0,len(message)):
        num_ans = message[num].isnumeric()
        if(num_ans == True):
            output += "A"
            output += (num2words(message[num]))
            output += "A"
        else:
            output += message[num]
    print(*output)      