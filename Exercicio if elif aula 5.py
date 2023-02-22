# Exercrcio 1
A = int(input("escolha um numero inteiro:"))
B = int(input("escolha outro numero inteiro:"))
C = int(input("escolha outro numero inteiro:"))

if A > B and A > C:
    print("O maior é: ",A)
elif B > C and B > A :
    print("O maior é: ",B)
elif C > B and C > A:
    print("O maior é: ",C)

if B>A>C or C>A>B:
    print (" O Valor intermediario é: ", A)
    
elif C>B>A or A>B>C:
    print (" O Valor intermediario é: ", B)
   
elif A>C>B or B>C>A:
    print (" O Valor intermediario é: ", C)

if A < B and A < C:
    print("O menor é: ",A)
elif B < C and B < A :
    print("O menor é: ",B)
elif C < B and C < A:
    print("O menor é: ",C)



# Baskhara

print ("formula de Baskhara")
N1 = int(input("escolha um numero inteiro:"))

if N1 == 0:
    print("erro")
else:
    N2 = int(input("escolha outro numero inteiro:"))
    N3 = int(input("escolha outro numero inteiro:"))

Delta = (N2**2) - 4*N1*N3

import math

Raiz = Delta**0.5

if Delta < 0:
    print("Delta Negativo")
    
elif Delta==0:
    Raiz0 =-N2/2*N1
    print (" a unica raiz é: ",Raiz0)
    
elif Delta>0:
    Raiz1= (-N2 + Raiz)/2*N1
    Raiz2= (-N2 -Raiz)/2*N1
    print (" As Raizes são: ",Raiz1,Raiz2)
