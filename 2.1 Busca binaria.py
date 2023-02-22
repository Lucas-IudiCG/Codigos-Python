vetor=[1,2,7,15,23,56,57,58,70,72,78]

def buscaSequencial1(vetor,x):
    cont=0
    for i in range(len(vetor)):
        cont+=1 #conta quantidade de comparações
        if vetor[i] == x:
            print("quantidade de passos--> ",cont)#se achou!
            return i
    print("quantidade de passos--> ",cont) #se não achou!
    return -1;


def buscaSequencialOrdenada(vetor,x):
    cont=0
    for i in range(len(vetor)):
        cont+=1
        if vetor[i] == x:
            print("quantidade de passos--> ",cont)
            return i
        else:
            if x < vetor[i]:
                return -1

def busca1(v,x):
    left=v[0]
    right=v[len(v)-1]
    middle=(left+right)//2
    k=0
    for i in range(len(v)):
        if x>middle and x<right:
            left = middle+1
            middle = (left+right)//2
            k+=1
        
        
        elif x<middle and x>left:
            right = middle-1
            middle = (left+right)//2
            k+=1


        elif x== middle:
            k+=1
            print("Número de passos: ",k)
            return x

        elif x==left:
            k+=1
            print("Número de passos: ",k)
            return x

        elif x==right:
            k+=1
            print("Número de passos: ",k)
            return x
    


M=int(input("Numero da busca: "))
print(buscaSequencial1(vetor,M))
