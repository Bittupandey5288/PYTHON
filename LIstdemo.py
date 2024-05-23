print("List object is given below")
list1=["Tata","HDFC","Realince",100,200]
print("The list element is ",list1)
# Methods of List
list1.append(300)
print("append method ",list1)
last=list1.pop()#remove the last item from the list
print(list1)
print(last)
# remove the specific element from the list item
list1.remove("Tata") # remove operation
print("After removing the element",list1)
# reverse() the list item 
list1.reverse()
print("reverse =",list1)
# insert() the element in the list at specific index
list1.insert(1,"hello")
print(list1)
#extend()the anothe list item in list1
list2=["Black","Red","Orange"]
list1.extend(list2)
print(list1)
ind=list1.index("Black")
print(ind)



