words = ['can','dog','watch']
attempt = 0
my_word = ""
for word in range(0,len(words)):
    my_word = words[word]
    print("\33[1;35mguess the word ",(word+1))
    print("\33[1;34mit is a " + str(len(my_word)) + " letter word")
    while(attempt < 5):
        input_word = input("\33[1;37menter your guess = ")
        if(len(input_word) == len(my_word)):
            for letter in range(0,len(input_word)):
                if(input_word[letter] == my_word[letter]):
                    print("\33[0;32m",input_word[letter],end="")
                elif(input_word[letter] in my_word):
                    print("\33[0;33m",input_word[letter],end="")
                else:
                    print("\33[0;31m",input_word[letter],end="")
            print()
            if(my_word == input_word):
                print("\33[1;32myou won")
                break
        else:
            print("\33[1;31minvalid word")
        attempt += 1
    if(my_word != input_word):
        print("\33[1;31myou lose")
        break
    attempt = 0