from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

cursor.execute("""
    SELECT last_name, SUM(net_worth) FROM UserDetail
    GROUP BY last_name
""")

a = cursor.fetchall()
print(a)