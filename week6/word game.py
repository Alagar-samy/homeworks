attempts = 0
index = 0
input_word = ""
my_word_list = ['can','dog','watch'] # store the words in a list 
result = False
for word in range(0,len(my_word_list)):
    print("letters are h, a, d, w, g, n, t, c, o")
    my_word = my_word_list[word]
    print("find word " + str(word+1))
    print("it is a " + str(len(my_word_list[word])) + " letter word")
    while(attempts < 10):
        input_letter = input("enter the letter = ")
        if(input_letter == my_word[index]):
            print(input_letter,"green")
            index += 1
            input_word += input_letter
        elif(input_letter in my_word):
            print("yellow")
            print("your letter is correct but in the wrong position")
        else:
            print("red")
            print("your letter is wrong")
            print("try different letter")
        attempts += 1
        if(input_word == my_word):
            result = True
            break
    if(result == True):
        print(my_word + " matches " + input_word)
        print("``` you won!!! ```")
    else:
        print("~~~ too many attempts ~~~")
        print(" XXX you failed XXX")
    input_word = ""
    index = 0
    result = False
    attempts = 0