from threading import Thread
# threading is module Thread is class 
class A(Thread):
    def run(self):
        for i in range(5):
            print("Task of run method ")
class B(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
obj=A()
obj.start()
obj1=B()
obj1.start() # start method will call the run method internally
