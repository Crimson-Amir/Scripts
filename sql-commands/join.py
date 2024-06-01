"""
INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL JOIN
"""

from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()


cursor.execute(f"""
    SELECT * FROM UserDetail as e1 LEFT JOIN Product as e2 ON e1.UserID = e2.UserID 
""")

fetch = cursor.fetchall()
print(fetch)