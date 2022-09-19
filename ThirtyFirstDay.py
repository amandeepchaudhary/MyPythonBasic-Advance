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
# os.mkdir('mydirThirtyFirstDay/mydirChild')
print()


#DATABASE

#establishing the connection>>>>>>>>>
import mysql.connector
# syntax==
# obj_Name=mysql.connector.connect(user==username'root',password='aman',host='localhost',port=3306)
conn=mysql.connector.connect(
    user='root',
    password='aman',
    host='localhost',
    port=3306
)
#by using Disctionary

config={        #we can write anything at config's place
    'user':'root',
    'password':'aman',
   'host':'localhost',
    'port':'3306'
}
try:        #extra>>>>><<<<<<<<<<<
    conn=mysql.connector.connect(**config)      #creating a connection>>
    if(conn.is_connected()):                    #checking the connection>
        print("Connected to the database MySQL")
except:
    print('Unable To Connect')

conn.close()                                    #Closing the connection>>
if(conn.is_closed()):                           #checking the connection closed>
    print('Connecttion Closed!')

#<<<<<<<<<<<<<<SKIPED THE DATABASE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







# Exception handling>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#try,except,else,finally
#try will try that the code will run or not,
# except will show the exception's solution in it,
# else will execute if try runs and exception didn'y occurs,
# finally will execute always

#We can use nested exception like if else and all>>
# Built-in Exceptions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a=10
b=0

try:
    r=a/g
    print(r)        #gives error so,
except ZeroDivisionError as obj:
    print("Obj of except gives info:",obj)
    print('Zero in the base is not Allowed')

except NameError:
    print('Data given variable is Wrong')
else:
    print('Inside Else as Try Portion is executed')

finally:
    print('Inside Finally As it Always Executes irrespective of any conditions')
print('Rest of the Code')

# user-made Exceptions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#if we want a user doesn't do that thing then we force it with exception
# and in built-in exceptions we have automatic raise system by errorclass and warningclass but as a programmer in user made exceptions we need to raise the exception ourself>>>> 

a=10
b=20

class BalanceException(Exception):
    pass

def checkbalance():
    money=5000
    withdraw=int(input('Enter the Amount to withdraw:'))
    balance=money-withdraw
    if (balance<=2000):
            raise BalanceException('Balance is not sufficient')
    print(balance)

try:
    checkbalance()
except BalanceException as be:
        print(be)
        # print("Balance Money:",balance)

#Assert condiition
a=10    #if true then assert exception statement not happen
assert a<=10,'Invalid1'

# a=20    #if false then assert excaprion statement happens
# assert a<=10,'Invalid2'
