def GeraLista(C,N):
    import random
    if C==1:
        X=0
        List=[]
        for i in range(N):
            List.append(X)
            X+=1
        return List
    elif C==2:
        List=[]
        for i in range(N):
            List.append(N)
            N-=1
        return List
    elif C==3:
        List=[]
        for i in range(N):
            List.append(random.randint(1,8))
        return List





def MergeSort(Lista,Inicio,Fim):
    if (Fim-Inicio)>1:
        Meio=(Inicio + Fim)//2
        MergeSort(Lista,Inicio,Meio)
        MergeSort(Lista,Meio,Fim)
        Merge(Lista,Inicio,Meio,Fim)

def Merge(Lista,Inicio,Meio,Fim):
    Esquerda= Lista[Inicio:Meio]
    Direita= Lista[Meio:Fim]
    Top_e,Top_d=0,0
    for k in range(Inicio,Fim):
        if Top_e>= len(Esquerda):
            Lista[k]=Direita[Top_d]
            Top_d+=1
        elif Top_d>= len(Direita):
            Lista[k]=Esquerda[Top_e]
            Top_e+=1
        elif Esquerda[Top_e]< Direita[Top_d]:
            Lista[k]=Esquerda[Top_e]
            Top_e+=1
        else:
            Lista[k]= Direita[Top_d]
            Top_d+=1



            
def main():
    N=int(input("Tamanho da lista: "))
    Lista1= GeraLista(1,N)
    MergeSort(Lista1,0,len(Lista1))
    print(Lista1)
    for r in range(5):
        print("")
    Lista2= GeraLista(2,N)
    MergeSort(Lista2,0,len(Lista2))
    print(Lista2)
    for r in range(5):
        print("")
    Lista3= GeraLista(3,N)
    MergeSort(Lista3,0,len(Lista3))
    print(Lista3)



main()
