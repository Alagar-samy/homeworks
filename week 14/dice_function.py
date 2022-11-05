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
board_1 = []  
board_2 = []

for r in range(0,8): # for displaying purpose
    inner = []
    for c in range(0,8):
        if( r == 0 or r == 7 or c == 0 or c == 7):
            inner.append("")
        else:
            inner.append("-")
    play_board.append(inner)

for r in range(0,8): # creating board for player 1
    inner = []
    for c in range(0,8):
        if( r == 0 or r == 7 or c == 0 or c == 7):
            inner.append("")
        else:
            inner.append("-")
    board_1.append(inner)

for r in range(0,8): # creating board for player 2
    inner = []
    for c in range(0,8):
        if( r == 0 or r == 7 or c == 0 or c == 7):
            inner.append("")
        else:
            inner.append("~")
    board_2.append(inner)

print("DICE BOARD")
for i in range(0,len(play_board)):
    for j in range(0,len(play_board[i])):
        print(play_board[i][j],end = " ")
    print()
    
def play(user_name, opp_user_name, my_board, opp_board, play_board,  my_point, opp_point, row, column): # function to play the game
    print("the generated row for you  : ",row)
    print("the generated column for you  : ",column)
    play_board[row][column] = user_name
    my_board[row][column] = user_name
    
    for i in range(0,len(play_board)): # displaying the board
        for j in range(0,len(board_1[i])):
            print(play_board[i][j],end = " ")
        print()
    
    if(opp_board[row][column] == opp_user_name): # if my row and  column of opponent's board have the opponent name
        my_point += 1 # i get 1 point
        print(user_name + ", your points : " + str(my_point))
        if(opp_point > 0): 
            opp_point -= 1 # opponent loses 1 point
        print(opp_user_name + ", your points : " + str(opp_point))
    elif((opp_board[row - 1][column] == opp_user_name) or 
         (opp_board[row + 1][column] == opp_user_name) or 
         (opp_board[row][column - 1] == opp_user_name) or 
         (opp_board[row][column + 1] == opp_user_name)): # if i my  spot is within one row or column of opponent's spot
        opp_point += 1 # opponent gets 1 point
        print(opp_user_name + ", your points : " + str(opp_point))
        if(my_point > 0):
            my_point -= 1 # i lose 1 point
        print(user_name + ", your points : " + str(my_point))
    if(my_point >= 5): # if my point is greater than or equal to 5
        print("you won ",user_name) # i won the game and the game stops 
        exit()
    elif(opp_point >= 5): # if opponent's point is more greater than or equal to 5
        print("you won ",opp_user_name) # opponent won the game and the game stops
        exit()
        
def dice(row,column,user_1_name,user_2_name): # function to get the rows annd columns from the players
    print("its your turn ",user_1_name)
    response = input("enter something to roll the dice : ")
    row = random.randint(1,6) # generate random number for row
    column = random.randint(1,6) # generate random number for column
    play(user_1_name, user_2_name, board_1, board_2, play_board, user_1_points, user_2_points, row, column) # call the play function to paly the game for player 1
    print("its your turn ",user_2_name) 
    response = input("enter something to roll the dice : ")
    row = random.randint(1,6) # generate random number for row
    column = random.randint(1,6) # generate random number for column
    play(user_2_name, user_1_name, board_2, board_1, play_board, user_2_points, user_1_points, row, column) # call the play function to paly the game for player 2
    dice(row, column, user_1_name, user_2_name) # call the dice function again

dice(row, column, user_1_name, user_2_name) # call the dice function