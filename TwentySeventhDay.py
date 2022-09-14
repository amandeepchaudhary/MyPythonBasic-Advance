#Abstract class

from abc import ABC,abstractclassmethod

class Father(ABC):
    @abstractclassmethod
    def show(self):
        pass
    
    def show(self):
        print("Concrete Method")
        