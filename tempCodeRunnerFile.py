with open('AmanFileHandling.txt',mode='r') as f1:
    data=f1.read()
    print(data)
    print(f1.closed)
print(f1.closed)