from math import*

km = float(input('Digite a quantidade de quilômetros rodados:'))
dias = float(input('Digite quantos dias de aluguel:'))
pt = (dias * 60) + (km * 0.15)
print('O Preço a pagar será de: ' , pt)