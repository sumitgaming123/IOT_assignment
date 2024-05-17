import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

empid = int(input("enter empid:"))
name = input("enter name:")
email = input("enter email:")
department = input("enter department:")
salary = int(input("enter salary:"))
date  = input("enter date:")

query = f"insert into employe values({empid},'{name}','{email}','{department}',{salary},'{date}');"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()


