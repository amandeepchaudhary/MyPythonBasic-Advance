import pickle,student123

with open('student1.dat',mode='rb') as f:
    #we dont know how many students the user will enter so,
    while True:     #by this we ran out of input EOFError so,
        try:        #Exception handling
            obj=pickle.load(f)     #converting binary to Text
            obj.show_details()
        except EOFError:
            print("Done Reading!!!")
            break
    
    print('UnPickling Done!!!!!!!!')
    