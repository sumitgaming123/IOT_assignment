import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
    )

def update_employe(empid, name):
    conn = get_connection()

    query = f"updates employe SET empid = %s where name = %s;"
    val = (name, empid)

    cursor = conn.cursor()
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()

update_employe("Pushpa", 99)