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
user_1_row = -1
user_1_column = -1
user_2_row = -1
user_2_column = -1
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
    
    
while True:
            
    print("its your turn " + user_1_name  + " >>")
    response = input("enter yes to play : ")
    user_1_row = random.randint(1,6) # generate random number for row  
    user_1_column = random.randint(1,6) # generate random number for column
    print("the generated row for you  : ",user_1_row)
    print("the generated column for you  : ",user_1_column)

    board_1[user_1_row][user_1_column] = user_1_name # store the name to user-1's personal board
    play_board[user_1_row][user_1_column] = user_1_name  # store the name to display board

    for i in range(0,len(play_board)): # displaying the board
        for j in range(0,len(board_1[i])):
            print(play_board[i][j],end = " ")
        print()
        
    if(board_2[user_1_row][user_1_column] == user_2_name): # check the row  and column as same occur in the user-2's board
        user_1_points += 1 # user-1 gets points
        print( user_1_name + " points  = " ,user_1_points)
        if(user_2_points > 0):
            user_2_points -= 1 # user-2 loses his 1 point 
        print( user_2_name + " points  = " ,user_2_points)
    elif((board_2[user_1_row - 1][user_1_column] == user_2_name) or 
         (board_2[user_1_row + 1][user_1_column] == user_2_name) or 
         (board_2[user_1_row][user_1_column - 1] == user_2_name) or 
         (board_2[user_1_row][user_1_column + 1] == user_2_name)): # checking the spot of user-2 within one row or column of user-1
        user_2_points += 1 # user-2 gets the poiunt
        print( user_2_name + " points  = " ,user_2_points)
        if(user_1_points > 0):
            user_1_points -= 1 # user 1 loses the point
        print( user_1_name + " points  = " ,user_1_points)
    
    if(user_1_points >= 5):# user-1 has more than or equal to 5 points
        print("you won " + user_1_name + " !!!") # user-1 won the match and break the game
        break
    elif(user_2_points >= 5):# user-2 has more than or equal to 5 points
        print("you won " + user_2_name + " !!!") # user-2 won the match and break the game
        break
            
            
    print("now its your turn " + user_2_name + " >>")
    response = input("enter yes to play : ")
    user_2_row = random.randint(2,6) # generate random number for row 
    user_2_column = random.randint(2,6) # generate random number for column 
    print("the generated row for you  : ",user_2_row)
    print("the generated column for you  : ",user_2_column)

    board_2[user_2_row][user_2_column] = user_2_name # store the name to user-2's personal board
    play_board[user_2_row][user_2_column] = user_2_name # store the name to display board
    

    
    for i in range(0,len(play_board)): # displaying the board
        for j in range(0,len(play_board[i])):
            print(play_board[i][j],end = " ")
        print()
        
    if(board_1[user_2_row][user_2_column] == user_1_name): # check the row  and column as same occur in the user-2's board
        user_2_points += 1 # user-2  gets point
        print( user_2_name + " points  = " ,user_2_points)
        if(user_1_points > 0):
            user_1_points -= 1 # user-1 loses 1 points
        print( user_1_name + " points  = " ,user_1_points)
    elif((board_1[user_2_row - 1][user_2_column] == user_1_name) or 
         (board_1[user_2_row + 1][user_2_column] == user_1_name) or 
         (board_1[user_2_row][user_2_column - 1] == user_1_name) or 
         (board_1[user_2_row][user_2_column + 1] == user_1_name)):# checking the spot of user-1 within one row or column of user-2
        user_1_points += 1 # user-1 gets the point
        print( user_1_name + " points  = " ,user_1_points)
        if(user_2_points > 0):
            user_2_points -= 1 # user-2 loses the point
        print( user_2_name + " points  = " ,user_2_points)

    if(user_1_points >= 5): # user-1 has more than or equal to 5 points
        print("you won " + user_1_name + " !!!") # user-1 won the match and break the game
        break
    elif(user_2_points >= 5): # user-2 has more than or equal to 5 points
        print("you won " + user_2_name + " !!!")# user-2 won the match and break the game 
        break