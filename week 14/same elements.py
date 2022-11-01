'''
THere are two arrays of numbers. the numbers are sorted in ascending order. 
Find the numbers that are common in both arrays. 
Eg - array 1 = [1,3,7,9,13,14,15], array2 [1,2,7,13,15]. answer - [1,7,13]
'''

# get two list
# comparing the elements one by one
# print the matching elements

list_1 = [1,3,7,9,13,14,15]
list_2 = [1,2,7,13,15,1]
ans_list = []

for index in range(0,len(list_1)):
    for check in range(0,len(list_2)):
        if(list_1[index] == list_2[check]):
            ans_list.append(list_1[index])
            break
            
print(ans_list)

