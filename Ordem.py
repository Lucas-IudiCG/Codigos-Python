import random
import time


n=int(input("Tamanho da Vetor: "))
def geraVetor(C,n):
    if C==1:
        vetor=[]
        N1=1
        for i in range(n):
            vetor.append(N1)
            N1+=1
    elif C==2:
        vetor=[]
        N1=n
        for i in range(n):
            vetor.append(N1)
            N1-=1


    elif C==3:
        vetor= []
        for i in range(n):
            N1=random.randint(1,n)
            vetor.append(N1)

    return vetor
def BubbleSort(V):
    Trocas=0
    Comparacao=0
    for i in range(len(V)):
        for j in range(i+1,n):
            if V[i]>V[j]:
                N1=V[i]
                V[i]=V[j]
                V[j]=N1
                Trocas+=1
            Comparacao+=1
    return V,Comparacao,Trocas


def SelectionSort(V):
    Trocas=0
    Comparacao=0
    for i in range(len(V)-1):
        min=i
        for j in range(i+1,len(V)):
            if V[min]>V[j]:
                min= j
                Comparacao+=1
        if min !=1:
            N1=V[i]
            V[i]=V[min]
            V[min]=N1
            Trocas+=1
    return V,Comparacao,Trocas

def InsertionSort(V):
    Trocas=0
    Comparacao=0
    for i in range(1,len(V)):
        x=V[i]
        j=i-1
        Comparacao+=1
        while j>=0 and x<V[j]:
            Trocas+=1
            V[j+1]=V[j]
            j-=1
        V[j+1]=x
    return V,Comparacao,Trocas

def main():
    print("Ordem 1")
    print("Bubble Sorts:")
    B1=geraVetor(1,n)
    RB1,ComparacaoB,TrocasB=BubbleSort(B1)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoB)
    print("Trocas: ",TrocasB)
    print("")
    
    print("Selection Sort:")
    S1=geraVetor(1,n)
    RS1,ComparacaoS,TrocasS=SelectionSort(S1)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoS)
    print("Trocas: ",TrocasS)
    print("")

    print("Insertion Sort:")
    I1=geraVetor(1,n)
    RI1,ComparacaoI,TrocasI=InsertionSort(I1)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoI)
    print("Trocas: ",TrocasI)
    print("")
    
    for a in range(5):
        print("")
    print("Ordem 2")
    print("Bubble Sorts:")
    B2=geraVetor(2,n)
    RB2,ComparacaoB,TrocasB=BubbleSort(B2)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoB)
    print("Trocas: ",TrocasB)
    print("")


    print("Selection Sort:")
    S2=geraVetor(2,n)
    RS2,ComparacaoS,TrocasS=SelectionSort(S2)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoS)
    print("Trocas: ",TrocasS)

    print("Insertion Sort:")
    I2=geraVetor(2,n)
    RI2,ComparacaoI,TrocasI=InsertionSort(I2)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoI)
    print("Trocas: ",TrocasI)
    print("")

    for a in range(5):
        print("")
    print("Ordem 3")
    print("Bubble Sorts:")
    B3=geraVetor(3,n)
    RB3,ComparacaoB,TrocasB=BubbleSort(B3)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoB)
    print("Trocas: ",TrocasB)
    print("")


    print("Selection Sort:")
    S3=geraVetor(3,n)
    RS3,ComparacaoS,TrocasS=SelectionSort(S3)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoS)
    print("Trocas: ",TrocasS)
    print("")

    print("Insertion Sort:")
    I3=geraVetor(3,n)
    RI3,ComparacaoI,TrocasI=InsertionSort(I3)
    print(f"Tempo decorrido: {time.process_time()}")
    print("Comparações: ",ComparacaoI)
    print("Trocas: ",TrocasI)
    print("")


main()
