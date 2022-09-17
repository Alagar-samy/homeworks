width = int(input("enter the width of the square = "))
for row in range(1,width+1):
    for column in range(1,width+1):
        if(row == 1 or row == width or column == 1 or column == width):
            print("*",end= " ")
        else:
            print(" ",end= " ")
    print()
    
    
 output:
   
* * * * *
*       *
*       *
*       *
* * * * *
