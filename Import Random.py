
# Exercicio 3

import random

X= str(input(" Escolha: Pedra, Papel ou Tesoura "))

C2= (random.choice(["Pedra","Papel","Tesoura"]))

X1= str.upper(X)

if X1 =="PEDRA":
    C1 = "Pedra"
    print("Você Colocou: ",C1)
    
elif X1 == "PAPEL":
    C1 = "Papel"
    print("Você Colocou: ",C1)
    

elif X1 =="TESOURA":
    C1 = "Tesoura"
    print ("Você Colocou: ",C1)
    

else:
    C1 = "Erro"
    print("Erro")



if C1 == "Pedra" and C2 == "Tesoura" or C1 == "Tesoura" and C2 =="Papel" or C1 == "Papel" and C2 == "Pedra":
    print("Computador Colcou:" ,C2)
    print("Você Venceu")

elif C2 == "Pedra" and C1 == "Tesoura" or C2 == "Tesoura" and C1 =="Papel" or C2 == "Papel" and C1 == "Pedra":
    print("Computador Colcou:" ,C2)
    print ("Você Perdeu")
    

elif C1 == C2:
    print("Computador Colcou:" ,C2)
    print("EMPATE")


