# Vetores

import random

vetor= [0]*10

def geraVetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = random.randint(1,100)
    return vetor


def imprimeVetor(vetor):
    for i in range(len(vetor)):
        print(vetor[i], end =" ")


def calculaMedia(vetor):
    soma=0
    for i in range(len(vetor)):
        X= vetor[i]
        soma=soma+X
    Y= len(vetor)
    media=soma/Y
    return media


def inverteVetor(vetor):
    vet1 =[0]*10
    vet2=[0]*10
    H= len(vetor)
    for i in range(len(vetor)):
        H= H-1
        vet1=vetor
        vet2[i]=vet1[H]
        print(vet2[i], end=" ")
    return vet2


vet = geraVetor(vetor)
imprimeVetor(vet)
print("Media:",calculaMedia(vet))
inverteVetor(vet)


