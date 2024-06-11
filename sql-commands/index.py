from connect import connect_client


"""
when column value don't change much
when data is big, don't use index for small table 
"""


a = connect_client().getconn()
cursor = a.cursor()

cursor.execute('BEGIN;')

cursor.execute("""
    CREATE INDEX IF NOT EXISTS first_name_index ON UserDetail (first_name)
""")

cursor.execute("""
    SELECT * FROM UserDetail 
""")

insert_to_db = cursor.fetchall()
print(insert_to_db)

cursor.execute("""
    DROP INDEX first_name_index 
""")

a.commit()
