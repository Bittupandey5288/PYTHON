class A:
    age=20
    #paramitrised constructor
    def __init__(self,name,adress):
        print("My name is ",name)
        print("My adress is ",adress)
        print("age is =",self.age)
obj=A("Ideal","kolkata")
class B:
    "Ideal insurance broker"
    def __init__(self):
     print("default constructor :")
ob=B() #default constructor would be atuotometically called
number=5
for x in range(5):
   print(x)
   x=x+1
   print(x)

   # multiple inheritance concept
class father:
     age=24
     def fun1(self):
      print("father class method")

class mother:
     name="sanju"
     def fun2(self):
       print("Mother class method") 

class child(father,mother):
   def child1(self):
      print(self.age,self.name)
o=child()
o.child1()#method calling

#single inheritanc concept
class insurance:
   company="ideal"
   def show(self):
      print("my company name is ideal broker pvt Ltd:")
class bike(insurance):
     def disp(self):
        print(self.company)
        self.show() #function calling of inside disp method
obj1=bike()# object creation 
obj1.disp()


        
   


        