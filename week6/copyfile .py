'''file = open("C:\\Users\win\Documents\sayur\week6\\alagar.txt","r")
print(file.read())
file.close()'''


file1 = open("C:\\Users\win\Documents\sayur\week6\\alagar.txt","r")
file2 = open("C:\\Users\win\Documents\sayur\week6\\copy.txt","w")
print(file1.read())
for  x in file1:
    file2.write(x)
file1.close()