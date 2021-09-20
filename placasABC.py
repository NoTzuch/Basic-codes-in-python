QA = int(input("Quantidade de A: "))
QB = int(input("Quantidade de B: "))
QC = int(input("Quantidade de C: "))

NA = QA // 2 #5 PLACAS
NB = QB // 3 #3 PLACAS
NC = QC // 7 #8 PLACAS
QP =NA #QP=5

if (NB<QP): #(3<5)
    QP=NB # QP=3

if (NC<QP): #(8<3)
    QP=NC # NAO SERA EXECUTADA

print("Quantidade maxima de placas: ", QP)



