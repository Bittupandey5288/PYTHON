#overriding
class A:
    def show(self):
        print("parent class dif method")
class B(A):
     def show(self):
        super().show() # super method is used to call the super class show method
        print("child class dif method")
ob=B()
ob.show()# child class method calling


# method overloading 
'''
Method overloading is not supported in python it will called last sum method 
with three argument list
'''
class Add:
    def sum(self,a,b):
        print(a+b)
    def sum(self,a,b,c):
        print("product of the number",a*b*c)
ob=Add()
#ob.sum(12,12) #function calling not possible argument not matching this line will give the error better comment it
ob.sum(1,2,3)        
