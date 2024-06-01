from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

cursor.execute("""
    create table if not exists UserDetail (
        userID serial PRIMARY KEY,
        first_name TEXT UNIQUE,
        last_name TEXT DEFAULT 'unknown',
        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        hire DATE NOT NULL DEFAULT CURRENT_DATE,
        class_number integer CHECK (class_number > 0 and class_number <= 50),
        name VARCHAR(50) CONSTRAINT name_length CHECK (length(name) > 2),
        net_worth money,
        CONSTRAINT net_worth_min_max CHECK (net_worth::numeric > 100.00 and net_worth::numeric < 1000.00)
    )
""")

a.commit()