import mysql.connector as mysql
conn = mysql.connect(user="root",password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("use shraddha")
c.execute("Drop database shraddha")
c.execute("SHOW DATABASES")
print(c.fetchall())
conn.close()
