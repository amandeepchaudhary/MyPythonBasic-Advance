#Infinite While Loop
i=0
while(True):
    i+=1
    print("Aman",i)
    if(i== 5):
        break
print("Rest of the code")

#Nested While Loop

i=1
while i<=2:
    print("Outer Loop",i)
    i+=1
    j=1
    while(j<=5):
        print("Inner Loop",j)
        j+=1
print("REst of the Code")

#range() Function
a = range(-1,-10,-2)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#For Loop
st = "CodeWithAman"
for ch in st:
    print(ch)
print("Rest of the Code")
                #OR with range
st = "CodeWithAman"
n = len(st)
print(n)
for i in range(n):
    print(i,"=",st[i])
print("Rest of the Code")

#For Loop With range()
a=range(5)
for i in a:
    print(i)
                #OR
for i in range(1,10,3):
    print(i)
print("Rest of the Code")

#For Loop with Else
string = "CodeWithAman"
r= len(string)
for name in range(r):
    print(string[name],name,sep="=")
else:
    print("Else Part")
print('Rest of the Code')

#Nested for Loop
for i in range(2):
    print("Outer For Loop")
    for j in range (5):
        print("Inner For Loop")
print("Rest of the Code")

#Break and Continue Statements
#Break Statement
for i in range(10):
    print(i)
    if(i==5):
        break
print("Rest of the Code")

#Continue Statement
for i in range(10):
    if(i==5):
        continue
    print(i)
print("Rest of the Code")

#Pass Statement
if 5<2:
    pass
else:
    print("Else Part")
print("Rest of the Code")

i=0
while i<10:
    if(i==5):
        pass
    print(i)
    i+=1 
print("Rest of the Code")