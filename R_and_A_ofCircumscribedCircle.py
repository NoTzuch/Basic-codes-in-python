from math import *
a = float(input("Enter the value of a segment: " ))
b = float (input("Enter the value of another segment: "))
hip = sqrt ((a**2) + (b**2))

print ("Radius: %.2f Area: %.2f" % (hip/2,pi*(hip/2)*(hip/2)))
