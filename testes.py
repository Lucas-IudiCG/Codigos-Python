#Testes
import random
import time


n=int(input("Tamanho da Vetor: "))
def SelectionSort(V):
    Trocas=0
    Comparacao=0
    for i in range(len(V)-1):
        min=i
        for j in range(i+1,len(V)):
            if V[min]>V[j]:
                min= j
                Comparacao=+1
        if min !=1:
            N1=V[i]
            V[i]=V[min]
            V[min]=N1
            Trocas+=1
    return V,Comparacao,Trocas


vetor1=[]
N1=1
for i in range(n):
    vetor1.append(N1)
    N1+=1

vetor2=[]
N1=n
for i in range(n):
    vetor2.append(N1)
    N1-=1



vetor3= []
VetorR= []
for i in range(n):
    N1=random.randint(1,n)
    vetor3.append(N1)

print(vetor3)
print("Selection Sort:")
vetorR,ComparacaoS,TrocasS=SelectionSort(vetor3)
print(f"Tempo decorrido: {time.process_time()}")
print("Comparações: ",ComparacaoS)
print("Trocas: ",TrocasS)
print("")
print(vetorR)
