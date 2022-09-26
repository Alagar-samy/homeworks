#own problem


import random
points = 0
attempts = 1
choose = ['r','p','s']
while(attempts <= 10):
    index = random.randint(0,2)
    print("\33[1;33m\33[1mattempt ",attempts)
    choice = input("\33[1;37menter your choice \33[1;35m\33[3m(rock - 'r' , scissors - 's', paper - 'p')\33[1;37m = \33[0m")
    print("system's choice = ",choose[index])
    if(choice == 'r' and choose[index] == 's'):
        print("\33[1;32myou won")
        points += 1
        attempts += 1
        print("\33[1;32mpoints = " + str(points) )
    elif(choice == 's' and choose[index] == 'r'):
        print("\33[1;31myou lose")
        attempts += 1
    elif(choice == 's' and choose[index] == 'p'):
        print("\33[1;32myou won")
        points += 1
        attempts += 1
        print("\33[1;32mpoints = " + str(points) )
    elif(choice == 'p' and choose[index] == 's'):
        print("\33[1;31myou lose")
        attempts += 1
    elif(choice == 'p' and choose[index] == 'r'):
        print("\33[1;32myou won")
        points += 1
        attempts += 1
        print("\33[1;32mpoints = " + str(points) )
    elif(choice == 'r' and choose[index] == 'p'):
        print("\33[1;31myou lose")
        attempts += 1
    elif((choice == 'p' and choose[index] == 'p') or (choice == 'r' and choose[index] == 'r') or (choice == 's' and choose[index] == 's')):
        print("\33[1;34mround draw")
    else:
        print("\33[1;31minvalid input")
print("                 \33[1;32myour score = ",points)
if(points >= 8):
    print("             \33[1;32mcongradulations!!!")
    print("         \33[1;32m\33[5m* * * * *\33[0m")
elif(points >= 5):
    print("             \33[1;34mgood")
    print("     \33[1;34m\33[5m * * *\33[0m")
elif(points >= 1):
    print("             \33[1;33mpoor")
    print("       \33[1;33m\33[5m * \33[0m")
elif(points == 0):
    print("       \33[1;31mbetter luck next time")
    print("      \33[1;31m\33[5mplay again\33[0m")
