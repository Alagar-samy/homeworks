'''write an app for the following two player game. you have a 6x6 board. user take turns rolling the dice twice. 
first roll is row num,second roll is column num. mark the spot (rows & columns) as claimed by the user who rolled the dice.
when the user roles the dice within 1 column or row of the claimed spot of the other user, the other user gets the point.
if the spot is same at the claimed point of the other user, the user that rolled the dice gets a point. the player who gets 5 points 
first will the  win the game.'''

import random

user_1_name = input("enter user 1 name : ")
user_2_name = input("enter user 2 name : ")
user_1_points = 0
user_2_points = 0
row = -1
column = -1
play_board =[] 

def creating_board (play_playboard): # this functiuon is for creating the board
    for r in range(0,8): 
        inner = []      
        for c in range(0,8):
            if( r == 0 or r == 7 or c == 0 or c == 7):
                inner.append("")
            else:
                inner.append("-")
        play_board.append(inner)
    return play_board


def display(play_board): # this function is for displaying the board
    for i in range(0,len(play_board)):
        for j in range(0,len(play_board[i])):
            print(play_board[i][j],end = " ")
        print() 
 
        
def generate_num(row,column): # this function generates row and column
    row = random.randint(1,6) # for generating row
    column = random.randint(1,6) # for generating column
    return row, column

def play (row,column,board,user_name,opp_user_name,my_points,opp_points): # this function checks the spot of both users
    print("the generated row for you  : ",row)
    print("the generated column for you  : ",column)
    
    if(board[row][column] == opp_user_name): # # if my row and  column of the board have the opponent name
        my_points += 1 # i get 1 point
        print(user_name + "'s point : ",my_points)
        if(opp_points > 0): # opponent player loses 1 point
            opp_points -= 1
        print(opp_user_name + "'s point : ",opp_points)
    elif((board[row - 1][column] == opp_user_name) or 
         (board[row + 1][column] == opp_user_name) or 
         (board[row][column - 1] == opp_user_name) or 
         (board[row][column + 1] == opp_user_name)): # if my spot is within one row or column of opponent's spot
        opp_points += 1 # opponent gets 1 point
        print(opp_user_name + "'s point : ",opp_points)
        if(my_points > 0):
            my_points -= 1 # i loses 1 point
        print(user_name + "'s point : ",my_points)
        
    board[row][column] = user_name # storing my name in the board
    
    if(my_points >= 5): # if my point is greater than or equal to 5
        print(" CONGRADULATIONS !!! YOU WIN THE GAME ",user_name) # i won the game and the game stops 
        exit()
    elif(opp_points >= 5): # if opponent's point is more greater than or equal to 5
        print(" CONGRADULATIONS !!! YOU WIN THE GAME ",opp_user_name) # opponent won the game and the game stops
        exit()
    return my_points, opp_points, board            
    
def main(user_1_name,user_2_name,row, column,user_1_points,user_2_points,play_board): # the main function starts here
    play_board = creating_board (play_board) # calling the function to create the borad
    display(play_board) # calling the funtion to displaying the board
    
    while True:
        
        print("its your turn ",user_1_name)
        response = input("enter something to play the game : ")
        row,column = generate_num(row,column) # calling the function to generate row and column
        user_1_points, user_2_points,play_board = play (row,column,play_board,user_1_name,user_2_name,user_1_points,user_2_points) # calling the function to check the spots and it will return both players points and current board
        display(play_board) # calling the function to displaying the board
        
        print("its your turn ",user_2_name)
        response = input("enter something to play the game : ")
        row,column = generate_num(row,column) # calling the function to generate row and column
        user_2_points, user_1_points,play_board = play (row,column,play_board,user_2_name,user_1_name,user_2_points,user_1_points) # calling the function to check the spots and it will return both players points and current board
        display(play_board) # calling the function to displaying the board
        
main(user_1_name,user_2_name,row, column,user_1_points,user_2_points,play_board) # calling the main function here



'''
ouput:


enter user 1 name : A
enter user 2 name : B
              
 - - - - - -  
 - - - - - -  
 - - - - - -  
 - - - - - -  
 - - - - - -  
 - - - - - -  
              
its your turn  A
enter something to play the game : A
the generated row for you  :  4
the generated column for you  :  1

 - - - - - -
 - - - - - -  
 - - - - - -
 A - - - - -
 - - - - - -  
 - - - - - -

its your turn  B
enter something to play the game : A
the generated row for you  :  4
the generated column for you  :  3

 - - - - - -  
 - - - - - -
 - - - - - -
 A - B - - -  
 - - - - - -
 - - - - - -  
        
its your turn  A
enter something to play the game : A
the generated row for you  :  1
the generated column for you  :  4

 - - - A - -
 - - - - - -
 - - - - - -
 A - B - - -
 - - - - - -
 - - - - - -

its your turn  B
enter something to play the game : A
the generated row for you  :  5
the generated column for you  :  2
        
 - - - A - -  
 - - - - - -  
 - - - - - -  
 A - B - - -  
 - B - - - -  
 - - - - - -  
        
its your turn  A
enter something to play the game : A
the generated row for you  :  6
the generated column for you  :  6

 - - - A - -  
 - - - - - -
 - - - - - -
 A - B - - -
 - B - - - -
 - - - - - A  
        
its your turn  B
enter something to play the game : A
the generated row for you  :  4
the generated column for you  :  2
A's point :  1
B's point :  0

 - - - A - -
 - - - - - -  
 - - - - - -
 A B B - - -  
 - B - - - -  
 - - - - - A

its your turn  A
enter something to play the game : A
the generated row for you  :  2
the generated column for you  :  4

 - - - A - -
 - - - A - -
 - - - - - -  
 A B B - - -  
 - B - - - -
 - - - - - A

its your turn  B
enter something to play the game : A
the generated row for you  :  2
the generated column for you  :  6

 - - - A - -
 - - - A - B
 - - - - - -
 A B B - - -  
 - B - - - -
 - - - - - A

its your turn  A
enter something to play the game : A
the generated row for you  :  5
the generated column for you  :  2
A's point :  2
B's point :  0

 - - - A - -
 - - - A - B  
 - - - - - -
 A B B - - -
 - A - - - -
 - - - - - A  

its your turn  B
enter something to play the game : A
the generated row for you  :  6
the generated column for you  :  4
        
 - - - A - -
 - - - A - B
 - - - - - -
 A B B - - -
 - A - - - -
 - - - B - A  

its your turn  A
enter something to play the game : A
the generated row for you  :  6
the generated column for you  :  4
A's point :  3
B's point :  0

 - - - A - -
 - - - A - B
 - - - - - -
 A B B - - -
 - A - - - -
 - - - A - A  

its your turn  B
enter something to play the game : A
the generated row for you  :  2
the generated column for you  :  4
B's point :  1
A's point :  2

 - - - A - -
 - - - B - B
 - - - - - -
 A B B - - -
 - A - - - -
 - - - A - A

its your turn  A
enter something to play the game : A
the generated row for you  :  5
the generated column for you  :  6

 - - - A - -
 - - - B - B  
 - - - - - -  
 A B B - - -  
 - A - - - A
 - - - A - A

its your turn  B
enter something to play the game : A
the generated row for you  :  6
the generated column for you  :  1

 - - - A - -
 - - - B - B
 - - - - - -  
 A B B - - -  
 - A - - - A
 B - - A - A  

its your turn  A
enter something to play the game : A
the generated row for you  :  1
the generated column for you  :  2
        
 - A - A - -  
 - - - B - B
 - - - - - -
 A B B - - -  
 - A - - - A  
 B - - A - A

its your turn  B
enter something to play the game : A
the generated row for you  :  3
the generated column for you  :  2

 - A - A - -  
 - - - B - B
 - B - - - -  
 A B B - - -
 - A - - - A
 B - - A - A
        
its your turn  A
enter something to play the game : A
the generated row for you  :  4
the generated column for you  :  3
A's point :  3
B's point :  0

 - A - A - -
 - - - B - B
 - B - - - -
 A B A - - -  
 - A - - - A
 B - - A - A

its your turn  B
enter something to play the game : A
the generated row for you  :  6
the generated column for you  :  5
A's point :  4
B's point :  0

 - A - A - -  
 - - - B - B  
 - B - - - -
 A B A - - -
 - A - - - A
 B - - A B A
        
its your turn  A
enter something to play the game : A
the generated row for you  :  3
the generated column for you  :  1
B's point :  1
A's point :  3

 - A - A - -
 - - - B - B
 A B - - - -  
 A B A - - -
 - A - - - A
 B - - A B A  

its your turn  B
enter something to play the game : A
the generated row for you  :  4
the generated column for you  :  5

 - A - A - -  
 - - - B - B
 A B - - - -
 A B A - B -  
 - A - - - A
 B - - A B A

its your turn  A
enter something to play the game : A
the generated row for you  :  1
the generated column for you  :  1

 A A - A - -
 - - - B - B
 A B - - - -  
 A B A - B -
 - A - - - A  
 B - - A B A
        
its your turn  B
enter something to play the game : A
the generated row for you  :  1
the generated column for you  :  5
A's point :  4
B's point :  0

 A A - A B -  
 - - - B - B
 A B - - - -
 A B A - B -
 - A - - - A  
 B - - A B A

its your turn  A
enter something to play the game : A
the generated row for you  :  5
the generated column for you  :  4

 A A - A B -
 - - - B - B
 A B - - - -
 A B A - B -
 - A - A - A
 B - - A B A

its your turn  B
enter something to play the game : A
the generated row for you  :  2
the generated column for you  :  6

 A A - A B -
 - - - B - B
 A B - - - -
 A B A - B -
 - A - A - A
 B - - A B A
        
its your turn  A
enter something to play the game : A
the generated row for you  :  2
the generated column for you  :  5
B's point :  1
A's point :  3
        
 A A - A B -
 - - - B A B  
 A B - - - -
 A B A - B -
 - A - A - A
 B - - A B A

its your turn  B
enter something to play the game : A
the generated row for you  :  1
the generated column for you  :  3
A's point :  4
B's point :  0

 A A B A B -
 - - - B A B
 A B - - - -  
 A B A - B -
 - A - A - A
 B - - A B A
        
its your turn  A
enter something to play the game : A
the generated row for you  :  6
the generated column for you  :  3

 A A B A B -
 - - - B A B
 A B - - - -
 A B A - B -
 - A - A - A
 B - A A B A

its your turn  B
enter something to play the game : A
the generated row for you  :  6
the generated column for you  :  5
A's point :  5
B's point :  0
you won  A'''