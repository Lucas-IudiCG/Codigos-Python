vet=[0]

import random

def geraVetor1(A):
    size = int(input("Tamanho do Vetor: "))
    A=[0]*size
    for i in range (size):
        A[i] = random.randint(1,15)
    return A
    

def Uniao(A,B):
    resp=" "
    for i in range (len(A)):
        for j in range (len(B)):
            if A[i]== B[j]:
                resp= resp+ str(A)+ " "


            elif A[i]!= B[j]:
                resp= resp+ str(A)+ " "
                resp= resp+ str(B)+ " "
                    
    return resp

A=geraVetor1(vet)
B=geraVetor1(vet)
print(A)
print(B)
print(Uniao(A,B))
