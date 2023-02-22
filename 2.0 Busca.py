import random

vetor= [0]*10

def geraVetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = random.randint(1,5)
    return vetor

def busca1(v,x):
    k=0
    while k <len(v):
        if v[k]==x:
            return k
        k+=1

    return -1

def busca2(v,x):
    for k in range (len(v)):
        if v[k]==x:
            return k
        k+=1

    return -1

def busca3(v,x):
    for k in range (len(v)):
        if v[k]==x:
            return k
        k+=1

    return -1

def busca4(v,x):
    L=""
    for k in range (len(v)):
        if v[k]==x:
            K=str(k)
            L=L+" " +K
            print(L)
        k+=1
        cont=k+1
        

    return cont

# Apenas Ordenado
def busca5(v,x):
    m=0
    while v[m]< x and m <len(v):
        m+=1;
        if v(m) ==x:
            return m;
        else:
            return -1


def buscaOrdem(v,x):
    for i in range(len(v)):
        if v[i]==x:
            return i
        else:
            if x<v[i]:
                return -1
    return -1
    


vet=geraVetor(vetor)
print(vet)
print(buscaOrdem(vet,3))
