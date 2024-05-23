print("Hello")
def calculate(*args):
    print(type(args))
    print(args)
calculate(1,2,3,4,5)
class A:
    def m1(self,*args):
        print(type(args))
        print(args)
ob=A() # creating the object
ob.m1(1,2,3,4,5,6)# Method calling 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
print(thisdict)
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print("Data type",arr.dtype)
def dem1(a,b=20):
    print(a,b)

dem1(100) #calling
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3) # 4 rows with 3 columns  we will have 4 arrays

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)