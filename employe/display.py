
import mysql.connector
import dbconn

def display_all():
    connection = dbconn.get_connection()
    query = "select *  from employe order by empid;"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()  
    for t in records:
        print(t)
    cursor.close()
    connection.close()

def display_Dept():
    connection = dbconn.get_connection()
    dept = (input("Enter the Department :") ,)
    query = "select *  from employe where department = %s;"
    val = dept
    cursor = connection.cursor()
    cursor.execute(query,val)
    records = cursor.fetchall()  
    print(f"Employe from {dept}")
    for t in records:
        print(t)
    cursor.close()
    connection.close()



def display_highest_salary():
    connection = dbconn.get_connection()
    query = "select * from employe order by salary DESC;"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()  #RETURN LIST OF TUPLES
    print(f"Employe with higest salary")
    for t in records:
        print(t)
    cursor.close()
    connection.close()   

def display_lowest_salary():
    connection = dbconn.get_connection()
    query = "select * from employe order by salary;"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()  #RETURN LIST OF TUPLES
    print(f"Employe with lowest salary")

    for t in records:
        print(t)
    cursor.close()
    connection.close()

display_all()   
display_Dept()
display_highest_salary()
display_lowest_salary()