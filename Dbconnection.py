"""1.Install MySQL Driver
2.Create a connection Object
3.Create a cursor Object
4.Execute the Query"""
import mysql.connector
print("Driver is installed ")

# 2 create the connection object 
con_ob=mysql.connector.connect(host="localhost",user="root",password="demo",database="practice")
print("Connection created successfuly !",con_ob)
# create the cursor
cur_obj=con_ob.cursor()
print("Cursor object is created ",cur_obj)
"""cur_obj.execute("create table operations( E_name varchar(15),Age int,salary int);")
##print("Table created successfully !")"""
# See  how many tables are created in practice databse 
cur_obj.execute("show tables")

# us the loop stattement
for i in cur_obj:
    print(i)

