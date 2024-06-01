"""another name: set operations"""

from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

list_of_key = ['union', 'union all', 'intersect', 'except']

for key in list_of_key:
    print(key + ':')

    cursor.execute(f"""
        SELECT * FROM user_detail
        {key}
        SELECT userid,name FROM Product
    """)

    fetch = cursor.fetchall()
    print(f'{fetch} \n {len(fetch)} \n')