#1
class MyClass:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string:")

    def printString(self):
        print(self.string.upper())

s = MyClass()
s.getString()
s.printString()

#2
class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    
square = Square(4)
print("Area of square:", square.area())
    
#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 5)
print("Area of rectangle:", rectangle.area())
    
#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def show(self):
        print(f"Point: ({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
    
p1 = Point(0, 0)
p2 = Point(3, 4)
p1.show()
p2.show()
print("Distance between points:", p1.dist(p2))
    
#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balabce is {self.balance}.")
        else:
            print("Insufficient funds for withdrawal")

account = Account("John Doe", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

#6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13, 17, 19, 21]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)