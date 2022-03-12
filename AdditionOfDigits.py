from math import*

number=int(input("type a number of three digits: "))
a= number//100;
rest = number%100;
b = rest//10;
c= rest%10;
add=a+b+c;
print("add = ", add) 
