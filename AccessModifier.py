
from operators import add

class A:
    a=10 # public 
    _b=20 # protected
    __c=30 #private
    def access(self):
        print("inside method :")
        print(self.a)
        print(self._b)
        print(self.__c)
        print("Method end !")
obj=A()
obj.access() # method calling
print("outside the class public value ",obj.a)
print("outside the class protected value ",obj._b)
#print("outside the class public value ",obj.__c)
# Encapsulation means security hide the data from end user