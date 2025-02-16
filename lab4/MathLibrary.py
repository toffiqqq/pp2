import math 
#1
a = int(input("Input degree: "))
radian = math.radians(a)
print(f"Output radian: {radian}")

#2
height1 = int(input("Height:"))
first = int(input("First value:"))
second = int(input("Second value:"))

area1 = (first + second)/ 2 * height1
print(f"Expected output: {area1}")

#3
side = int(input("Number of sides:"))
length1 = int(input("Length of sides:"))

area2 = (side * length1 ** 2)/(4 * math.tan(math.pi / side))

print(f"Area of polygon: {area2}")

#4
length2 = int(input("Length of base: "))
height2 = int(input("Height of parallelogram: "))

area3 = length2 * height2
print(f"Area of parallelogram: {area3}")