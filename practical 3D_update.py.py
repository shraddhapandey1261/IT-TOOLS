import mysql.connector as mysql
conn = mysql.connect(user="root",password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("use shraddha")
c.execute("select  * from students")
rows=c.fetchall()
studid=rows[1][0]
print(studid)
c.execute("update students set sname='abc' where s_id=" +str(studid))
studid=rows[3][0]
print(studid)
c.execute("update students set sname='mno' where s_id=" +str(studid))
conn.commit
c.execute("select  * from students")
print(c.fetchall())
conn.close()
