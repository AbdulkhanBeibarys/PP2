#1
x = 300
def myfunc():
  x = 200
myfunc()
print(x)

#2
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
