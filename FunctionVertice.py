#Calculo do ex2
from math import*

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

Delta = (b*b)-4*a*b
x_v = -b/(2*a)
y_v = Delta/(4*a)

print('O ponto do Vertice é:', (x_v, y_v))


