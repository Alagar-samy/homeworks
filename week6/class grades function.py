# to find the average grade of a class in an particular subject
scores = []
total_student = int(input("enter the total students in a class = ")) 
for score in range(0,total_student): # to get students mark
    scores.append(int(input("enter the mark = ")))
mark = 0
total_marks = 0 
def grade (mark): # defining grade function
    if(mark > 90):
        print('grade A')
    elif(mark > 80):
        print('grade B')
    elif(mark > 70):
        print('grade C')
    elif(mark > 60):
        print('grade D')
    elif(mark < 60):
        print('fail')
for index in range(0,len(scores)):
    mark = scores[index]
    grade(mark) # calling the grade function to get grade for each students
    total_marks += mark
mark = total_marks / len(scores)
print("class average garde is = ",mark)
grade(mark) # calling the function to get grade the class for the subject