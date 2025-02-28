#1
import math

degree = float(input("Input degree:"))
radian = degree * (math.pi / 180)

print(f"Output radian: {radian:6f}")

#2
height = float(input("Height:"))
base1 = float(input("Base, first value:"))
base2 = float(input("Base, second value:"))

Area = (base1 + base2) / 2 * height

print(f"Output: {Area}")

#3
import math

n = int(input("Input number of sides:"))
m = float(input("Input the length of a side:"))

Area = (n * m ** 2) / (4 * math.tan(math.pi / n))

print(f"The area of polygon is: {Area}")

#4
a = float(input("Length of base:"))
b = float(input("Heigth of parallelogram:"))

Area = a * b
print(f"Output: {Area}")