import dbconn

def delete_employe(empid):
    conn = dbconn.get_connection()

    query = f"delete from employe where empid = %s;"
    val = (empid, )

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()


delete_employe(41)
