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





vet = geraVetor(vetor)
imprimeVetor(vet)
