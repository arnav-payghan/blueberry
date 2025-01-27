# ALL DATABASE CODES WILL BE ADDED HERE

import sqlite3

conn = sqlite3.connect("assistant.db")
cursor = conn.cursor()

# Creating a table sys command
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# Keep Null as it is (AutoIncrementing), 'name' add name for calling, 'path' add path by double file location in PC.
# query = "INSERT INTO sys_command VALUES (null, 'name', 'path')"
# cursor.execute(query)
# conn.commit()

# Create table : web_command
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# Keep Null as it is (AutoIncrementing), 'name' add name for calling, 'url' add url by copying said url.
query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()