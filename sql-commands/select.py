from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

cursor.execute("""
    SELECT DISTINCT name, COUNT(userID) FROM UserDetail
    WHERE NOT name = 'amir' AND userID BETWEEN 1 AND 20 
    GROUP BY name
    ORDER BY name 
""")

a = cursor.fetchall()
print(a)