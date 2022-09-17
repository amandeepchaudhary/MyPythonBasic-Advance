f=open('AmanFileHandling.txt',mode='r')
m1=f.readlines()
print(m1)
for i in m1:
    print(i,end='')
print(len(m1))
f.close()
print("Completed the Reading!!!!!!")