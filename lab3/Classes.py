class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

string_manipulator = StringManipulator()

string_manipulator.getString()

string_manipulator.printString()

#2 and 3
class Shape:
    def __init__(self):
        self.area_value = 0

    def area(self):
        print(f"Area of the shape: {self.area_value}")


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        self.area_value = self.length ** 2
        print(f"Area of the square: {self.area_value}")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  
        self.length = length
        self.width = width
    
    def area(self):
        self.area_value = self.length * self.width
        print(f"Area of the rectangle: {self.area_value}")

shape = Shape()
shape.area()  

square = Square(4)
square.area()

rectangle = Rectangle(4, 5)
rectangle.area()

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Point moved to: ({self.x}, {self.y})")

    def dist(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance


point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

point1.move(2, 3)

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

account = Account("Bill", 500)

account.deposit(50)  

account.withdraw(30)

account.withdraw(200)  

print(f"Current balance is {account.get_balance()}.")

#6
prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

nums = [2, 3, 8, 10, 11, 17, 21, 22, 23, 56, 89, 1]

prime_numbers = list(filter(prime, nums))

print(prime_numbers)