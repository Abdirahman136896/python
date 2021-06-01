#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math

radius = int(input("Enter the radius of the circle: "))
x= math.pi

#area = ((22/7) * pow(radius, 2))
area = (math.pi * pow(radius, 2))

print(area)