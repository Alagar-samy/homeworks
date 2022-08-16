students=int(input("enter total students in a class = "))
subjects=int(input("enter total subjects = "))
gpa=0
total_gpa=0
total=0
average_gpa=0
score=0
for student in range(1,students+1):
    print("student",student)
    for subject in range(1,subjects+1):
        score=int(input("enter the score = "))
        total+=score
    gpa=total/subjects    
    total_gpa+=gpa
    gpa=0
    total=0
average_gpa=total_gpa/students
print(average_gpa)