from array import *
stu_roll=array('i',[101,102,103,104,105,106,107])
print("Original Array")
n=len(stu_roll)
for J in range(n):
    print(J,"=", stu_roll[J])

print("***************************")
a=stu_roll[1:5]  #jha se shuru kiya wha se hoga and khtam ek pehle p hoga
for m in a:
    print(m)

print("***************************")
a=stu_roll[0:7:3]  #jha se shuru kiya wha se hoga and khtam ek pehle p hoga
for m in a:
    print(m)

print("***************************")
for J in stu_roll[1:5]:
    print(J)

print("***************************")