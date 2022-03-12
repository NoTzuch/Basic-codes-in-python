from math import*

numero=int(input("Digite um número de três algarismos:"))
a= numero//100;
resto = numero%100;
b = resto//10;
c= resto%10;
soma=a+b+c;
print("soma = ", soma) 
