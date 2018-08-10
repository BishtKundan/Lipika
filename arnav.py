print("Hello, World")

if 3 > 2:
	print(" 3 is greater than 2")
	
print ("Enter your name : ")
x=input()
print ("Hello " + x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#

def my_function():
  print("Hello from a function1")
  print("Hello from a function2")


my_function()

import platform

x = dir(platform)
print(x)

import datetime
x = datetime.datetime.now()
print(x)

print("JSON start")

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

f = open("TestFile.txt", "r")
print (f.read())
