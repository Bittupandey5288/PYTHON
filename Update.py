import mysql.connector
myconnection=mysql.connector.connect(
host="localhost",
user="root",
password="demo",
database="practice")
mycursor=myconnection.cursor()
update="update operations set E_name=%s where salary=%s"
dataval=("Dev",35000)
mycursor.execute(update,dataval)
myconnection.commit()
print("Data updated !")
                 