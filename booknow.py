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


Full_Name = form.getvalue("FullName")
Email = form.getvalue("Email")
Contact = form.getvalue("Contact")
Adults = form.getvalue("Adults")
Childrens = form.getvalue("Childrens")
Yes = form.getvalue("Yes")
No = form.getvalue("No")
Bus = form.getvalue("Bus")
Train = form.getvalue("Train")
Airplanes = form.getvalue("Airplanes")
Date = form.getvalue("Date")


con = mysql.connector.connect(user='root',password='',host='localhost',database='booknow')
cur = con.cursor()

cur.execute("insert into booking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Full_Name,Email,Contact,Adults,Childrens,Yes,No,Bus,Train,Airplanes,Date))
con.commit()

cur.close()
con.close()

print("<h1>  We will Contact you soon for further process!!!!</h1>")

