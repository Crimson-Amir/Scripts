
from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

# cursor.execute("""
#     create table if not exists Constraints (
#         id serial PRIMARY KEY,
#         class_number integer CHECK (class_number > 0 and class_number <= 50),
#         name varchar(50) CONSTRAINT name_length CHECK (length(name) > 2),
#         net_worth money,
#         CONSTRAINT net_worth_min_max CHECK (net_worth::numeric > 100.00 and net_worth::numeric < 1000.00)
#     )
# """)

cursor.execute("""
    insert into Constraints(class_number, name, net_worth) values (1, 'kir', 101.00)
""")

# cursor.execute("""
#     drop table Constraints
# """)

a.commit()