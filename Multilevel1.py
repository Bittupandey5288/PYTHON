# Multilevel inheritance 
class Grandfather:
     myname="Ranjan"
     def m1(self):
        print("Hi i am Garndfather")
class father(Grandfather):
    myname2="Raju"
    def m2(self):
        print("Hi i am your father")
class son(father):
    def m3(self):
        print("son method")
        print(self.myname, " ", self.myname2) 
obj=son() # through son class we can access the value of the grandfather and father
obj.m1()
obj.m2()
obj.m3()     

# Hirerichal inheritance

class Dad:
    def m1(self):
        print("Hi i am your father11")
class sonu(Dad):
    def m2(self):
        print("hi my father nam is X")
class sony(Dad):
      def m3(self):
          pass
#obj3=sonu()
#obj4=sony()
#obj3.m1() 
#obj4.m1()

#hydrid inheritance
class master1(sony):
     def mas(self):
        print("hi i am master method ")

obj4=sony()
obj4.m1()
obj4.mas()
    
    
