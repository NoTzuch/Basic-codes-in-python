p = int(input("Digite a quantidade  de parafusos: "))
cg= p//250
r1=p%250
cm=r1//50
r2=r1%50
cp=r2//10
vt=cg*8.50+cm*3.20+cp*1.80
print ("Caixas de tamanho grande: ", cg)
print ("Caixas de tamanho médio: ", cm)
print ("Caixas de tamanho pequeno: ", cp)
print ("Valor total: ",vt)

