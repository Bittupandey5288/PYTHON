import numpy as np
arr1=np.array([[10,20,30,40],[50,60,70,80]])
print("The dimension of the Array is",np.ndim(arr1))
array1=np.array([100,200,300,400,500,600,700,800,900])
print(np.ndim(arr1))
# performe Action with Array
# 1 shape method mainly tells about how much row and column in your Array
print("shape of the array ",array1.shape)
# 2 reshape the Array
newarr=array1.reshape(3,3)
print("New Array shape ",newarr.shape)
"""
Try converting 1D array with 8 elements to a 
2D array with 3 elements in each dimension (will raise an error):
"""
#itreating
for i in array1:
    print("iterate array element ",i)