#1
class MyClass:
  x = 5

#2
class MyClass:
  x = 5
p1 = MyClass()

#3
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#5
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()