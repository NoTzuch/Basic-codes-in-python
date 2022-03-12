pag=int(input("Quantas páginas deseja imprimir?:"))
stotal=(pag//5)*60
HORAS=stotal//3600
resto=stotal%3600
MIN=resto//60
SEG=resto%60
print("Demora",HORAS,"horas, ",MIN,"minutos e",SEG,"segundos")


-------outro codigo------------
# pag -> numero de paginas
# H -> Horas
# M -> Minutos
# S -> segundos

pag=int(input("Entre com o numero de páginas: "))
temp=pag*12
H=temp//3600
resto=temp%3600
M=resto//60
S=resto%60


print("Tempo horas:",H)
print("Tempo minutos:",M)
print("Tempo segundos:",S)
