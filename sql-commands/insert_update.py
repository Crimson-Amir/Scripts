from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

cursor.execute("""
    INSERT INTO Product (name, price, userID) 
    VALUES ('mous', 40.80, 5) RETURNING *
""")

insert_to_db = cursor.fetchall()
print(insert_to_db)
a.commit()


# cursor.execute("""
#     UPDATE UserDetail SET last_name = 'whalberg', class_number = 12 WHERE userID = %s RETURNING *
# """, (insert_to_db[0][0],))
#
#
# insert_to_db = cursor.fetchall()
# print(insert_to_db)

a.commit()
