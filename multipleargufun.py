
def calculateTotalSum(*arguments):
    print(type(arguments))
    totalSum = 0
    for number in arguments:
        print(number)
        totalSum += number
    print(totalSum)
 
# function call
calculateTotalSum(5, 4, 3, 2, 1)
sum=0
tup=(10,10,10,10,10)
for i in tup:
    sum=sum+i
    print(i)
    print("Sum of list object ",sum)
    