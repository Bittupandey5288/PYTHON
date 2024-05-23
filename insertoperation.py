import mysql.connector
print("Driver is loaded :")

#create the connection object

mycon=mysql.connector.connect(
host="localhost",
user="root",
password="demo",
database="practice"
    )
print("Conncetin established ")

# 2 create the cursorobject
mycursor=mycon.cursor()
# 3 Execute the query using cusor object
# perform insert operation in tables 
mycursor.execute("insert into operations values('Piku',24,35000);")
mycon.commit() # use the commit
print("Data inserted in table")
