#!C:\Users\HP\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-type: text/html")
print()
import cgi,cgitb
import mysql.connector

print("<h1>Registration Confirmation Message</h1>")
print("<hr>")
print("<h1>Using Input Tag</h1>")
print("<body bgcolor='Grey'>")

form = cgi.FieldStorage()

First_Name = form.getvalue("FirstName")
Last_Name = form.getvalue("LastName")
Email = form.getvalue("Email")
Contact = form.getvalue("Contact")
Username = form.getvalue("Username")
Password = form.getvalue("Password")
Confirm_Password = form.getvalue("ConfirmPassword")

con = mysql.connector.connect(user='root',password='',host='localhost',database='registration')
cur = con.cursor()

cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Email,Contact,Username,Password,Confirm_Password))
con.commit()

cur.close()
con.close()

print("<h1>Your account has been registered successfully. We will Contact you soon for further process!!!</h1>")

    