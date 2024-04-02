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
product_id, INTEGER ,
user_id, INTEGER)
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

dp_connect.commit()

dp_connect.close()
