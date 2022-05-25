from unicodedata import name
import pymysql as sql

def getConnection():
    return sql.connect(host="localhost", user="root", passwd="", database="student_details")

def insertData(t):
    con = getConnection()
    cur = con.cursor()
    query = "insert into Student_Info(name, email, gender, contact, dob, address) values (%s,%s,%s,%s,%s,%s)"
    cur.execute(query,t)
    con.commit()
    con.close()

def showData():
    con = getConnection()
    cur = con.cursor()
    query = "select * from Student_Info"
    cur.execute(query)
    f = cur.fetchall()
    con.commit()
    con.close()
    return f

def deleteData(id):
    con = getConnection()
    cur = con.cursor()
    query = "delete from Student_Info where id = %s"
    cur.execute(query,(id,))
    con.commit()
    con.close()