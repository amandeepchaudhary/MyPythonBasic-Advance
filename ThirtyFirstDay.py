#Pickling and Unpickling>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Pickling is a process of converting a class object into a byte stream so that it can be stored into a file
#also called object serialization
# we use pickle module to perform pickling and unpickling
#unpickling is just a reverse of pickling module called as de-serialization
#pickle module is not secure against erroneous or maliciously contructed data
#never Unpickle data recieved from an untrusted or un authenticated source
#pickling==dump(),,,, unpickling==load()
#main===pick kro data ko binary m change kro then load kro text mai

import pickle
class Students:
    def __init__(self,name,roll_no,classs,address):
        self.n=name
        self.rn=roll_no
        self.c=classs
        self.a=address
    
    def show_details(self):
        print(f'Name:{self.n} ,Roll_no:{self.rn} ,Class:{self.c} ,Address:{self.a}')

with open('student.dat',mode='wb') as f:
    s=Students('Aman', 22, 5, 'Canada')
    pickle.dump(s,f)
    print('Pickling Done!!!!!!!!!')

with open('student.dat',mode='rb') as f:
    obj1=pickle.load(f)
    print('UnPickling Done!!!!!!!!')
    obj1.show_details()


#Directory=os module==used to perform simple operation on directories
# os.getcwd() ==know current directory
# mkdir('dirname')==used to make a directory
# mkdir('parentdirectory/childdirectory')=used to create a child directory
# mkdirs('parent/child/grandchild')=used to create a child a grandchild Directory
# chdir('dirname')=to change current directory
# rename('oldname','newname')=to rename a directory
# rmdir('dirname')=to remove a directory
# rmdirs('parent/child')=to remove all directory
# walk()=used to know the contents of directory,returns iterator whose objects can be displayed using for loop

import os
print(os.getcwd())#^^^^^^^^^^^^^^^^^^^^ can impliment all ^^^^^^^^^^^^^^^^^^^^
os.mkdir('mydirThirtyFirstDay/mydirChild')


#DATABASE