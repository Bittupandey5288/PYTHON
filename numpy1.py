import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
#a1=np.array([["*"],["**"],["***"]])
print(a)
print("Dimension of the Array ",a.ndim)
for i in a:
    print(i)
# Joinig Array Element #
print("Joining Array Element !")
arr1 = np.array([1, 2, 3])
sum=0
for i in arr1:
    j=0
    sum=sum+arr1[j]
    j=j+1
print("Sum of Array element ",sum)
print("The element of the Array is ",arr1[1])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
arr2=np.array([[1,2,3],[4,5,6]])
print("Dimension of the Array ",arr.ndim)
print(arr2.ndim)


#for i in arr:
list =[1,2,3,4,5]
sum1=0
for i in list:
    sum1=0
    sum1=i+sum1
    print("The sum of the ",sum1)     