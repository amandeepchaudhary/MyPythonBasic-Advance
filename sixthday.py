#Slicing on Arrays
from array import *
stu_roll=array('i',[101,102,103,104,105,106,107])
print("Origanal array")
# print(stu_roll)
n=len(stu_roll)
for elements in range(n):
    print(elements,"=",stu_roll[elements])