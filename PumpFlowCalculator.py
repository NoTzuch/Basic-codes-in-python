from math import*
# c -> capacidade do reservatório e v -> vazao da bomba
# Ts(total de segundos) = c//v

c=int(input("Digite a capacidade do reservatório: "))
v=int(input("Digite a vazão da bomba: "))
Ts=c//v
qh= Ts//3600
resto = Ts%3600 #resto em segundos descontadas as horas
qm = resto//60  # numero de minutos
qs = resto%60   # numero de segundos



print("Tempo ", qh, " : ", qm, " : ", qs)

