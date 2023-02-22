import random

X= str(input(" Escolha: Pedra, Papel ou Tesoura "))

C2= (random.choice(["Pedra","Papel","Tesoura"]))

X1= str.upper(X)

if X1 =="PEDRA":
    C1 = "Pedra"
    print(C1)
    
elif X1 == "PAPEL":
    C1 = "Papel"
    print(C1)
    

elif X1 =="TESOURA":
    C1 = "Tesoura"
    print (C1)
    
