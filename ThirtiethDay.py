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

#tell() and seek() Method==========>>>>>>>>>>>>>>
f=open('AmanFileHandling.txt')