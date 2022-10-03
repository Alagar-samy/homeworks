# to store the list words for comparing the input
words = ['can','dog','watch']
my_word = ""
# to compare the words one by one using loop
for word in range(0,len(words)):
    attempt = 0 # to set the variable as attempt for the game's limit
    my_word = words[word]
    # to print the characters with the specified colors using ansi codes
    print("\33[1;35mguess the word ",(word+1)) 
    print("\33[1;34mit is a " + str(len(my_word)) + " letter word")
    while(attempt < 5): # attempts starts 
        input_word = input("\33[1;37menter your guess = ") # get the input word from the user
        if(len(input_word) == len(my_word)): # checking the length of both user's input and my word 
            for letter in range(0,len(input_word)): # cheching the input word with letter by letter
                if(input_word[letter] == my_word[letter]): # matching the input word's letter and the position is same it displays green color 
                    print("\33[0;32m",input_word[letter],end="")
                elif(input_word[letter] in my_word): # matching the letter is in the my word  but in wrong position it displays yellow color
                    print("\33[0;33m",input_word[letter],end="")
                else: # if the letter and the position doesn't matches it displays red in color
                    print("\33[0;31m",input_word[letter],end="")
            print()
            if(my_word == input_word): # if input word and my word is equal it displays you won 
                print("\33[1;32myou won")
                break
        else: # length of the both words not equal it prints invalid input
            print("\33[1;31minvalid word")
        attempt += 1
    if(my_word != input_word):
        print("\33[1;31myou lose")
        break