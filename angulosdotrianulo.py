alfa = int(input("Digite o valor do angulo alfa: "))
beta = int(input("Digite o valor do angulo beta: "))
if (alfa+beta)<180:
    gama = 180-alfa-beta
    print ("O valor de gama eh", gama) 
if alfa==90 or beta==90 or gama==90:
    print ("Triangulo Retanguloo!")
else:    
    if alfa>90 or beta>90 or gama>90:
     print ("Trianglo Obtusangulo")
#else: 
    #print("Triangulo Actangulo!")
#else: 
    #print ("nao sao angulos internos de um triangulo")


