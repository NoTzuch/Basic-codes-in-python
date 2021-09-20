from math import *
a = float(input("Digite o valor de um cateto: " ))
b = float (input("Digite o valor de outro cateto: "))
hip = sqrt ((a**2) + (b**2))

print ("Valor do raio: %.2f Valor da area: %.2f" % (hip/2,pi*(hip/2)*(hip/2)))