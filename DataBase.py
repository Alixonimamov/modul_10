import sqlite3

dp_connect = sqlite3.connect("Alixon.sqlite3")

dp_cursor = dp_connect.cursor()

dp_cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
first_name REAL,
last_name TEXT)
""")

dp_cursor.execute("""
CREATE TABLE IF NOT EXISTS product(
id INTEGER PRIMARY KEY,
title TEXT,
price REAL)
""")

dp_cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY,
product_id INTEGER ,
user_id INTEGER)
""")

dp_cursor.execute("""
INSERT INTO users ("first_name", "last_name")
VALUES("Alixon", "Imamov")
""")

dp_cursor.execute("""
INSERT INTO users ("first_name", "last_name")
VALUES("Paul", "Maker")
""")

dp_cursor.execute("""
INSERT INTO users ("first_name", "last_name")
VALUES("Jordan", "Jeffrey" )
""")

dp_cursor.execute("""
    INSERT INTO product(title, price) VALUES ('apple', 500)

""")

dp_cursor.execute("""
    DROP TABLE orders
""")

def alter_users():
    dp_cursor.execute("""
    ALTER TABLE  users ADD COLUMN age INTEGER DEFAULT 10
    """)
    dp_cursor.execute("""
    ALTER TABLE users RENAME yosh to age
    
    """)


def insert_product(title, price):
    dp_cursor.execute("""
    INSERT INTO product(title, price)
    VALUES (?, ?)""", (title, price))


def insert_orders(product_id, user_id):
    dp_cursor.execute("""
    INSERT INTO orders (prduct_id, user_id)
    VALUES(?, ?)""", (product_id, user_id))


def read_users():
    dp_cursor.execute("""
        SELECT * FORM users
         """)

def update_users():
    dp_cursor.execute("""
        UPDATE users SET first_name = 'Jon', last_name = 'Doe' WHERE id=1
    """)

def delete_users():
    dp_cursor.execute("""
        DELETE FROM users WHERE id=1
    """)


# dp_cursor.execute("SELECT * FORM users")

dp_connect.commit()

dp_connect.close()
