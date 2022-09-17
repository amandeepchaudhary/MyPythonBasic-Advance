import pickle,student123

inp=int(input('Enter the Number of Students:'))
with open('student1.dat',mode='wb') as f:
    for i in range(inp):
        name=input("Enter Student's Name:")
        roll_no=int(input("Enter Student's Roll_no:"))
        classs=int(input("Enter Student's Class:"))
        address=input("Enter Student's Address:")
        s=student123.Students(name,roll_no,classs,address)
        pickle.dump(s, f)

print('Pickling Done!!!!!!!!!')
