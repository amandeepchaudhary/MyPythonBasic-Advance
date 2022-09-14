# Tech package ---> work module

#Siblings concept == means the folders/ packages 
#for this taking the USer package's Request module and importing it in the Tech's
# work module
import User.request

a = "aman"
def tech_work():
    print(" Tech package ---> work module")
    print("tech_work module Function")
    print()
    
User.request.user_request()
b = "aman"

#for accessing the module file in tech work we need to see the tech.work file as a script so we
#use a flag named -m(mod) = which runs a module as a script so, we run this where we can see the both siblings means both the folders/packages in file explorer ,C:/users/ishu/desktop/pythonproject/smspackage= python -m Tech.work
#no need to add the .py extension
#we have a altternative as hack who don't know how to do this
#import sys
# sys.path.append('users package path==== c:/users/ishu/desktop/pythonproject/smspackage/user'), import request , request.user_request()
#this runs in Tech package location

# <<<<<<<<<<<<<<<<OR>>>>>>>>>>>>>>>>>

import sys
sys.path.append('C:/Users/ISHU/Desktop/PythonProject/SMSPackageTwentySixthDay/User')
import request
request.user_request()