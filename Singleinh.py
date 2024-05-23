class Parent:
    age1=30
    def m1(self):
        print("Hi i am parent class method ")
        print(self.age2)
class Son(Parent):
    age2=24
    def m2(self):
        print("My age is ",self.age2)

# object creation of the class
obj=Son()
obj.m1()
obj.m2() # calling the method of the parent class using child class object