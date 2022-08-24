from audioop import reverse


students=[]
total_students=int(input("enter the total students in a class = "))
for student in range(0,total_students):
    students.append(input("enter the student name = "))
#print(*students,sep="\n")
student=len(students) - 1
total_marks=0
average=0
'''
for student in range(student,-1,-1):
    print(students[student])
    '''
for marks in range(0,total_students):
    mark=int(input(str(students[marks]) + " scored = "))
    total_marks+=mark
average = total_marks / total_students
print("class average = ",average)

student=len(students) - 1
for student in range(student,-1,-1):
    print(students[student])