pag=int(input("Numero de paginas:"))
stotal=(pag/5)*60
HORAS=stotal//3600
resto=stotal%3600
MIN=resto//60
SEG=resto%60
print("Demora",HORAS,"horas, ",MIN,"minutos e",SEG,"segundos")