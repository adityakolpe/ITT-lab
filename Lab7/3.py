#!C:\Python27\python.exe
import sqlite3
import cgi

conn=sqlite3.connect('passwords.db')

#conn.execute("CREATE TABLE pwdTable (username VARCHAR PRIMARY KEY, password VARCHAR);")
conn.execute("INSERT INTO pwdTable VALUES('aditya', 'aditya');")
conn.execute("INSERT INTO pwdTable VALUES('aditi', 'aditi');")
conn.execute("INSERT INTO pwdTable VALUES('shaury', 'shaury');")
conn.execute("INSERT INTO pwdTable VALUES('tinder', 'tinder');")

form=cgi.FieldStorage()

loginId=form.getvalue('loginId')
pwd=form.getvalue('pwd')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Result</title>")
print ("</head>")
print ("<body>")

valid=0

cursor=conn.execute("SELECT * FROM pwdTable")

for row in cursor:
	if row[0]==loginId and row[1]==pwd:
		valid=1
if valid==1:
	print ("<h1>Login successful</h1>")
else:
	print ("<h1>Login unsuccessful</h1>")

print ("</body>")
print ("</html>")

conn.commit()
conn.close()
