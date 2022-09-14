#One dimensional array module
#index after Type Codes
# import array as ar
from array import *
stu_roll=array('f',[101,102,103,104.4,105])
print(stu_roll[3])

#Accessing array using For Loop
for elements in stu_roll:
    print(elements)

n=len(stu_roll)
for elements1 in range(n):
    print("index",elements1,"=",stu_roll[elements1])

#Accessing Array using While Loop
print('Accessing Array using While Loop')
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1

#Append Method
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
print("Array after Append")
stu_roll.append(106)
stu_roll.append(107)
print(stu_roll[5])    
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1

#Getting User Input
stud_roll=array('i',[])
n=int(input('How many Elements you want to add?'))
for i in range(n):
    stud_roll.append(int(input('Enter the Element:')))

for i in range(len(stud_roll)):
    print("The",i,"Element","=",stud_roll[i])

#Getting input from User using While Loop
print("Getting input from User using While Loop")
student_roll= array('i',[])
n=int(input("How many elements?"))
i=0
while i<n:
    student_roll.append(int(input("Enter the elements:")))
    i+=1

j=0
r=len(student_roll)
while j<r:
    print("the",j,"Element =",student_roll[j ])
    j+=1

student_roll.insert(0,100)
print(student_roll[0])
n=len(student_roll)
for elements2 in range(n):
    print("The elements after insert is:")
    print(student_roll[elements2])

#POP() method of array
st_roll=array('f',[101,102,103,104,105])
n=len(st_roll)
i=0
while i<n:
    print(st_roll[i])
    i+=1
print("Array after POP")
st_roll.pop()       #this will remove the last element i.e.,105
n=len(st_roll)
j=0
while j<n:
    print(st_roll[j])
    j+=1

#pop(n)
st_roll.pop(0)
print(st_roll[0])

#remove() = remove the first occurence of the given array
print('remove() = remove the first occurence of the given array')
st_roll.remove(102)
n=len(st_roll)
k=0
while k<n:
    print(st_roll[k])
    k+=1

#Index() method
print(st_roll.index(104))

#Reverse() method
print("Reverse array")
st_roll.reverse()
n=len(st_roll)
l=0
while l<n:
    print(st_roll[l])
    l+=1

#extend() method == add another array after the first array
arr= array('f',[110,120,130])
n=len(st_roll)
i=0
while i<n:
    print(st_roll[i])
    i+=1

print('Array after Extend')
st_roll.extend(arr)
n=len(st_roll)
j=0
while j<n:
    print(st_roll[j])
    j+=1

