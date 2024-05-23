import numpy as np
arr=np.array([10,20,30])
print(arr)
print(type(arr))
#create Multidimensional Array
arr1=np.array([[10,20,30,40],[50,60,70,80],[90,100,200,300]])
print("Multidimensional Array are given below")
print(arr1)
 #slicing with array
arr2=np.array([100,200,300,400,500])
print("slicing is =",arr2[0:3])
# some Attributes of Array
arr3=np.array([[500,600,700,800,900],[1000,2000,3000,4000,5000]])
print(np.shape(arr3))
print(np.size(arr3))
print(np.ndim(arr3)) # What is the dimension of the arry it tells about that
print(arr3.dtype)
print(arr3.size) #it returs how many no of element in the arr3