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





def QuickSort(Lista,Inicio,Fim):
    if Inicio<Fim:
        Pivo=Partition(Lista,Inicio,Fim)
        QuickSort(Lista,Inicio,Pivo-1)
        QuickSort(Lista,Pivo+1,Fim)

def Partition(Lista,Inicio,Fim):
    Pivo= Lista[Fim]
    i=Inicio
    for j in range(Inicio,Fim):
        if Lista[j]<=Pivo:
            Lista[j],Lista[i]=Lista[i],Lista[j]
            i+=1
    Lista[i],Lista[Fim]=Lista[Fim],Lista[i]
    return i



            
def main():
    N=int(input("Tamanho da lista: "))
    Lista1= GeraLista(1,N)
    QuickSort(Lista1,0,len(Lista1)-1)
    print(Lista1)
    for r in range(5):
        print("")
    Lista2= GeraLista(2,N)
    QuickSort(Lista2,0,len(Lista2)-1)
    print(Lista2)
    for r in range(5):
        print("")
    Lista3= GeraLista(3,N)
    QuickSort(Lista3,0,len(Lista3)-1)
    print(Lista3)



main()
