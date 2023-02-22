import random

def fat(n):
    if n==1:
       return 1
    else:
        return n*fat(n-1)



n=int(input())
print(fat(n))


def somaLista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0]+ somaLista(lista[1:])

lista=[]*n
for i in range(n):
    x=random.randint(1,10)
    lista.append(x)
    print(lista)

print(somaLista(lista))


def rfunc(n):
    if n==0:
        return 0
    else:
        return rfunc(n-1) +2


print(rfunc(n))
