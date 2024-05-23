import mysql.connector
myconnection=mysql.connector.connect(
host="localhost",
user="root",
password="demo",
database="practice"
)
print("Coonection created Successfully")
Mycursor=myconnection.cursor()
print("cursor object created !")
query="delete from operations where salary=35000"
#setvalue=(17000)
Mycursor.execute(query)
myconnection.commit()
print("Row deleted Successfully !")


