# interface contain only abstract method
# we can not create the object of the interface
from abc import ABC,abstractmethod
class insurance(ABC):
    @abstractmethod
    def SI(self):
        pass
    # another abstract method
    @abstractmethod
    def claim(self):
        pass # here pass means you will implement this method Later
class Ideal(insurance):
    def SI(self):
        print("The Sum insured of the Insurance is 50 thousand")

    def claim(self):
        print("The insured received the claim amount only 40 thousand ")
# object creation 
obj=Ideal()
obj.SI()# methoid calling 
obj.claim() # method calling
#oj=insurance() #Can't instantiate abstract class insurance without an implementation for abstract methods 'SI', 'claim'
oj.claim()