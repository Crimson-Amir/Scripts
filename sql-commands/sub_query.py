from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

cursor.execute("""
    SELECT first_name FROM UserDetail
    WHERE userID in (SELECT userID from Invoice WHERE invoiceID > 10)
""")

a = cursor.fetchall()
print(a)