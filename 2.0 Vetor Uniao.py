import random

Size1= int(input("Tamanho do Primeiro vetor: "))
Size2= int (input("Tamanho do Segundo vetor: "))
A=[0]* Size1
B=[0]* Size2



def geraVetor(vetor):
    for i in range(len(vetor)):
        vetor[i]=random.randint(1,10)
    return vetor


def uniao(A,B):
    Solucao =" "
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i]==B[j]:
                if A[i]==B[j]:
                    Solucao=Solucao +str(A[i]) + " "
    return Solucao

    



print(geraVetor(B))
print(geraVetor(A))
print(uniao(A,B))
