import cgi, cgitb
import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=BES01L4KBISHT\SQLEXPRESS;"
                      "Database=hellodb;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
cursor.execute('select firstname,lastname from employee')

print('Content-Type: text/plain')
print('')
#print('Hello, world!')

for row in cursor.fetchall():
	print(row)

cursor.execute('select firstname,lastname from employee')	
for row in cursor.fetchall():
	print(row[0])
