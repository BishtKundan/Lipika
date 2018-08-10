print('Content-Type: text/html')
print('')
print('<h1><u>Server side app using Python</u></h1>')

import datetime
x = datetime.datetime.now()
print("<strong>Today  </strong> is  : " + x.strftime('%m/%d/%Y'))

print("<br /><br /><u>Following text is read from file TestFile.txt</u><br /><br />")
f = open("TestFile.txt", "r")
print (f.read())