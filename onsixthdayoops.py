#after slicing in core python i started oops in advance python
#class and object
#Example 1
class Myclass(object):
    def show(self):   #instance variable nhi chahiye tha isliye def liya
        print("I am a Method")

x= Myclass()
x.show()

#Example 2
class Myclass:
    def show(self):   #instance variable nhi chahiye tha isliye def liya
        print("I am a Method")

x= Myclass()
x.show()

#Example 3
class Mobile:
    def __init__(self):
        self.model ="RealMe X"
        self.price = 10000

    def show_model(self):
        print("Model:",self.model,"Price=",self.price)

realme = Mobile()
realme.show_model()
print(realme.model)
realme.model = 'RealMe X7 Max'
realme.price = 30000
print(realme.model)
realme.show_model()
print(realme.price)
realme.show_model()

#Example 4
class Phone:
    def __init__(self,p):
        self.phone = p
    def show_model_n_price(self,m,p):
        model = m
        price = p
        print('Phone:',self.phone,'Model:',model,"Price=",price)
realMe=Phone('Realme X7 Max')
realMe.show_model_n_price("RMX3031",29999)
print(id(x))
print()

redMi=Phone('RedMI 10')
redMi.show_model_n_price('readmi 3400', 24000)
print(id(redMi))
print()

aman = Phone('Python')
aman.show_model_n_price('vscode', 20000)
print(id(aman))

