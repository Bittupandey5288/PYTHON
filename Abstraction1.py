# Python abstraction  when the action is common but implemention is diff use abstra
from abc import ABC,abstractmethod
class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")
    @abstractmethod
    def speed(self):
        pass
class bike(Car):
   def speed(self):
       print("bike speed is 70 km/h")
class maruti(Car):
   def speed(self):
       print("bike speed is 100 km/h")

obj=bike()
obj1=maruti()
obj1.speed()
obj.speed() #method calling

# use abstraction class when action is common but implemention is diff use abstraction


