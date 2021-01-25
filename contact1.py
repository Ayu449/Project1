#!C:\Users\HP\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-type: text/html")
print()
import cgi,cgitb
import mysql.connector

print("<h1>Submitted Succesfully.</h1>")
print("<hr>")
print("<h1>Using Input Tag</h1>")
print("<body bgcolor='Grey'>")

form = cgi.FieldStorage()

First_Name = form.getvalue("FirstName")
Last_Name = form.getvalue("LastName")
Email = form.getvalue("Email")
Contact = form.getvalue("Contact")
Message = form.getvalue("message")

con = mysql.connector.connect(user='root',password='',host='localhost',database='clickhere')
cur = con.cursor()

cur.execute("insert into contact values(%s,%s,%s,%s,%s)",(First_Name,Last_Name,Email,Contact,Message))
con.commit()

cur.close()
con.close()

print("<h1> We will Contact you soon!!!</h1>")

