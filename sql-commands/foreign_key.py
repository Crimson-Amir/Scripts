from connect import connect_client

a = connect_client().getconn()
cursor = a.cursor()

cursor.execute("""
    create table if not exists Product (
        productID serial PRIMARY KEY,
        name TEXT,
        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        price money CONSTRAINT price_min CHECK (price::numeric > 15.00),
        userID INT REFERENCES UserDetail(userID) ON DELETE CASCADE
    )
""")

a.commit()