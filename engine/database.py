# ALL DATABASE CODES WILL BE ADDED HERE

import csv
import sqlite3

conn = sqlite3.connect("assistant.db")
cursor = conn.cursor()

######################################## Creating a table SYS COMMAND ########################################

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

### Keep Null as it is (AutoIncrementing), 'name' add name for calling, 'path' add path by double file location in PC.

#query = "INSERT INTO sys_command VALUES (null, 'discord', 'C:\\Users\\arnav\\AppData\\Local\\Discord\\Update.exe')"
#cursor.execute(query)
#conn.commit()

######################################### Create table : WEB COMMAND #########################################

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

###### Keep Null as it is (AutoIncrementing), 'name' add name for calling, 'url' add url by copying said url.

#query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
#cursor.execute(query)
#conn.commit()

############################## Creating a table with the desired columns [CONTACTS] ##############################

#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

### Specifying column indices you want to import (0-based index)
### Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 18]

############ Reading the data from the CSV fole and inserting into SQLite table for desired columns ############

# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute('''INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# ### Committing the changes
# conn.commit()
# conn.close()

##########################################  ADDING A SINGLE CONTACT ##########################################

# query = "INSERT INTO contacts VALUES (null, 'Arnav', '9373697593', null)"
# cursor.execute(query)
# conn.commit()

##########################################  SEARCH CONTACT IN DATABASE ##########################################

# query = 'Arnav'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(query.upper() + "\'S NUMBER IS: " + results[0][0])