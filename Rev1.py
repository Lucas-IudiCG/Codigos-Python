import random


def geraVetor(X,n1,n2):
    Vet=[0]*X
    for a in range(X):
        N1=random.randint(n1,n2)
        Vet[a]=N1
    return Vet

def geraMatriz(X,Y,n1,n2):
    M=[]
    for i in range(X):
        N=[]
        for j in range(Y):
            N.append(random.randint(n1,n2))
        M.append(N)
    return M

def Inverte(Vet):
    B=len(Vet)
    Vet1=[0]*B
    for b in range(len(Vet)):
        B-=1
        N2=Vet[B]
        Vet1[b]=N2
    return Vet1

def Soma(Vet):
    SUM=0
    for c in range (len(Vet)):
        SUM+=Vet[c]
    return SUM

def MaiorMedia(Vet,SUM):
    X=len(Vet)
    D=0
    for d in range(X):
        if Vet[d]>(SUM/X):
            D+=1
    Vet1=[0]*D
    D1=D
    for d in range(X):
        if Vet[d]>(SUM/X):
            Vet1[D1-1]=Vet[d]
            D1-=1
    return D,Vet1

def InsertionSort(V):
    for i in range(1,len(V)):
        X=V[i]
        J=i-1
        while J>=0 and X<V[J]:
            V[J+1]=V[J]
            J-=1
        V[J+1]=X 
    return V

def Junta(A,B):
    H1=len(A)
    H2=len(B)
    B1=0
    A1=0
    R=[0]*(H1+H2)
    for i in range (H1+H2):
        if A[A1]>B[B1]:
            R[i]=B[B1]
            if B1<=48:
                B1+=1
        elif A[A1]<=B[B1]:
            R[i]=A[A1]
            if A1<=48:
                A1+=1
    return R

def Write(V):
    Write1=open("Valores.txt","w")
    for a in range(len(V)):
        Write1.write(str(V[a])+"\n")
        if a==(len(V)-1):
            Write1.write(str(V[a]))

def Read():
    Read= open("Valores.txt", "r")
    Final=False
    V=[]
    while Final==False:
        R=Read.readline()
        if R=="":
            Final=True
        else:
            R1 = R.rstrip()
            X=int(R1)
            V.append(X)
    V.remove(V[len(V)-1])
    Read.close()
    return V

def MatrizMaior(M,X,Y):
    SUM=0
    N1=0
    for i in range(Y):
        N1=0
        for j in range(X):
            N1+=M[i][j]
        if N1> SUM:
            L=i+1
            SUM=N1
    return SUM,L
    
def main():
    print("1")
    X=int(input("Número de notas: "))
    Vet=geraVetor(X,0,10)
    print("1.1: ",X)
    print("1.2: ",Vet)

    Vet1=Inverte(Vet)
    print("1.3: ",Vet1)
    SUM=Soma(Vet)
    print("1.4: ",SUM)
    print("1.5: ",SUM//X)
    D,VetD=MaiorMedia(Vet,SUM)
    print("1.6: ",D,VetD)

    print("2")
    A=geraVetor(50,1,100)
    A=InsertionSort(A)
    print("Primeiro vetor gerado:",A)
    B=geraVetor(50,1,100)
    B=InsertionSort(B)
    print("Segundo vetor gerado:",B)
    R=Junta(A,B)

    print("Resultado: ,",R)
    print(len(R))

    print("3")
    N=int(input("Número de valores aleatórios: "))
    W=geraVetor(N,1,100)
    print(W)
    Write(W)
    R1=Read()
    print(R1)
    R1=InsertionSort(R1)
    print(R1[0])
    print("4")
    print (R1[len(R1)-1])
    SUM=Soma(R1)
    X=len(R1)
    print("Média: ",SUM/X)


    print("5")
    M=geraMatriz(3,3,1,10)
    print(M)
    K,L=MatrizMaior(M,3,3)
    print(L,K)


    print("6")

    
    
main()
