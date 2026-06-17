# import sqlite3
# conn= sqlite3.connect('mydatabase.db')
# cursor= conn.cursor()
# cursor.execute('''
#                CREATE TABLE IF NOT EXIStS users(
#                    id INTEGER primary key,
#                    username TEXT  NOT NULL,
#                    age INTEGER,
#                    email text unique
#                 )
#        ''' )
# cursor.execute("INSERT INTO USERS(username,age,email)values('Alice',30,'alice@example.com')")
# conn.commit()

# insert multiple records
import sqlite3
conn= sqlite3.connect('mydatabase.db')
cursor= conn.cursor()
users=[
    ('Bob',25,'Hari@example.com'),
    ('Charlie',35,'Ram@example.com')

]
cursor.executemany("INSERT INTO users(username,age,email)values(?,?,?)",users)
conn.commit()
############################
#Retrive all records
# import sqlite3
# conn= sqlite3.connect('mydatabase.db')
# cursor= conn.cursor()
# cursor.execute("SELECT*from users")
# rows= cursor.fetchall()
# for row in rows:
#  print(rows)
###########################################
# import sqlite3
# conn= sqlite3.connect('mydatabase.db')
# cursor= conn.cursor()
# cursor.execute("SELECT*from users where age>30")
# rows= cursor.fetchall()
# for row in rows:
#  print(rows)

#update records ############################
# import sqlite3
# conn= sqlite3.connect('mydatabase.db')
# cursor= conn.cursor()
# cursor.execute("UPDATE users SET age=90 where username = 'Alice'")
# conn.commit()
#  #
 #update records ###########################
# import sqlite3
# conn= sqlite3.connect('mydatabase.db')
# cursor= conn.cursor()
# cursor.execute("Delete from users where username='Bob'")
# conn.commit()