width = int(input("enter the width of the square = "))
def square(width):
    for row in range(1,width+1):
        for column in range(1,width+1):
            print("*",end= " ")
        print()
square(width)

output:
    
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
