import mysql.connector

# creathe the connection
mycon=mysql.connector.connect(
host="localhost",
user="root",
password="demo",
database="practice"
    )
print("Conncetin established ")
# create the cursor object
mycursor=mycon.cursor()

# perform the query
mycursor.execute("select * from operations")
for tabledata in mycursor.fetchall():
    #Note:- fetchall method of cursor object is used to fetch all the row in the form of list of tupe
    print(tabledata)
print("----------------MY list of Tuple given below-------------------------")
list=[("Bittu",24),("Rahul",23),("Pandey",25)]
for i in list:
    print(i)
print("----------Tuple of the List we are creating below ---------")
t=([12,13,14],[40,50,60],["A","B","C"])
for TD in t:
    print(TD) 


