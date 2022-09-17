#File handling
# kabhi bhi koi data hamara abhi tak permanently store nhi hota tha pr aab hoga file ki madad se, file hum data store krne k liye banate hai mtlb hum koi user se input lete h toh data save hona chahiye h toh file voh data save krti h , bakki file chote projects k liye hota h bade projects mai Database and Cloud kaam aate hai
#two types of files - Text file( = used to store character and strings) and Binary File( =store data in the form of bytes,a group of 8 bits each, used to store text file, images, jpg, pdf, csv, video and audio)
# r=read only
# w=overwrite if file exits,if not exist then create and write
# x=create a new file and write in it, if file exists then shows an error
# a=used for appending the data mtln add kr deta h data ko existing data mai, if file doesnot exists then create a new file and wite the data in that file
# r+ = open for reading and then writing the data
# w+ = open for writing and then reading,it will overwrite the existing data
# a+ = open for appending then reading,it won't overwrite the existing data 

#Same for Binary bas(b add krna h)
# rb=read only
# wb=overwrite if file exits,if not exist then create and write
# xb=create a new file and write in it, if file exists then shows an error
# ab=used for appending the data mtln add kr deta h data ko existing data mai, if file doesnot exists then create a new file and wite the data in that file
# rb+ = open for reading and then writing the data
# wb+ = open for writing and then reading,it will overwrite the existing data
# ab+ = open for appending then reading,it won't overwrite the existing data 

#file_obj.name
#file_obj.mode
#file_obj.closed
#file_obj.readable()
#file_obj.writeable()
import os
if os.path.isfile('29d87d37d5e0a3d2d65aef4eef14729e.png'):
    f=open('29d87d37d5e0a3d2d65aef4eef14729e.png',mode='r')
    print("File Name:",f.name)
    print("Before File Close:",f.closed)
    print("File Mode:",f.mode)
    print("File Readable:",f.readable())
    print("File Writable:",f.writable())
    f.close()
    print("After File Close:",f.closed)
    print()
else:
    print("File png is not here")


#isfile = check file exists or not>>>>>>>>>>>>
import os
if os.path.isfile('AmanFileHandling.txt'):
    f=open('AmanFileHandling.txt')     #if we won't want to get ann error then
    print("File Opened")
    f.close
else:
    print("File Does not Exist")


#Writing Data in Files<<<<<<<<<<<ASLI GAME>>>>>>>>>>>>>>>>
f1=open('AmanFileHandling.txt',mode='a')    #x ko nyi gadi,w nyi gadi ko bar bar nyi banata hai,a nyi gadi ko use krte jata hai 
# lst1=['ok','lets','try']
n=f1.write(' kyaa haal hai bhai kkkkk!!!!!!!!!!')
# f1.write(lst1)  #this gives error must be str not list, so hume writelines likhna hai
print(n)
f1.close()
# print("Expriment")

#writelines() isse list,tuple,set etc sab kuch aa jata h
f=open('AmanFileHandling.txt','a')
lst=['Aman\n','Diksha\n','Sunita\n','Surender\n','Ishu\n']
f.writelines(lst)
f.close()
print("Success")
print()


#read is used to read character by character>>>>>>>>>>>>
f=open('AmanFileHandling.txt',mode='r')
m1=f.read(45)
m2=f.read(42)        #toh isme 45 character k baad k 4 character show honge
print(m1)
print(m2)
f.close()
print("Completed the Reading!!!!!!")
print("**********************")

#readline() is used to read a whole single line>>>>>>>>>>>>>
#readlines() is used to read all the lines and gives them as a List>>>>>>>>>>>>>

f=open('AmanFileHandling.txt',mode='r')
m1=f.readline()
m2=f.readline()        
print(m1,end=" ")  #end default "\n" hota hai 
print(m2)
f.close()
print("Completed the Reading!!!!!!")

#readlines()====
f=open('AmanFileHandling.txt',mode='r')
m1=f.readlines()
print(m1)
for i in m1:
    print(i,end='')
print(len(m1))
f.close()
print("Completed the Reading!!!!!!")
print()

#tell() Method = tell the location of the cursor in the file  and seek() Method = is used set the cursor at the needed location ==========>>>>>>>>>>>>>>
f=open('AmanFileHandling.txt', mode='r')
print(f.tell()) #location of the cursor is at the starting
data1=f.read(5) #after this the location of the cursor is at the 5th location
print(data1)
print(f.tell()) #shows the location 5 cause the cursor is at 5th
data2=f.read(14)
print(data2)
print(f.tell()) #the location of the cursor is at 19th
f.close()
print()

# p='nona non'
# print(p.title())


#seek(position)==
f=open('AmanFileHandling.txt',mode='r')
print(f.tell())
f.seek(5)
print(f.tell())
f.close()
print()

#r+,w+,a+ == Similar in rb+,wb+,ab+
#r+ = first read then write
f=open('AmanFileHandling.txt',mode='r+')
print(f.tell())
print(f.read())
print(f.tell())
f.write('Yoooo Boiiii!!!!!!!!')
print(f.tell())
f.close()
print()

#w+=== first write then read but with the help of seek method because after writing the cursor will be at the end and then read method comes so it eill be blank
f=open('AmanFileHandling.txt',mode='w+')
print(f.tell())
f.write('Yoooo Boiiii!!!!!!!!')
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read())
print(f.tell())
f.close()
print()

#a+ = first append then read with the help of seek method
f=open('AmanFileHandling.txt',mode='a+')
print(f.tell()) #will show at the end of the previous text
f.write('NOOOOOOOOOOOOOOOOOOOOOOO Yoooo Boiiii!!!!!!!!')
print(f.tell())
f.seek(0)
print(f.tell()) 
print(f.read())
print(f.tell())
f.close()
print()

#How to copy File Contents in python>>>>>>>>>>>>>>>>>>
f=open('AmanFileHandling.txt',mode='r') #Existing File
data=f.read()
print("***********************************************")
f1=open('AmanCopyFileHandling.txt',mode='w+')    #Copied File
f1.write(data)
f1.seek(0)
cdata=f1.read()
print(cdata)
f.close()
f1.close()
print()

#With Statement = with statement automatically Closed a open statement and used while opening a file>>>>>>>>>>>>>>>>>>>>>>>
# syntax:=====
# with open('file_name',mode='r') as file_obj:
#     statements like read write append exclusive and all

with open('AmanFileHandling.txt',mode='r') as f1:
    data=f1.read()
    print(data)
    print(f1.closed)
print(f1.closed)
