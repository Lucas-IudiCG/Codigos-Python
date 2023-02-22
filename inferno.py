A=0
divisores=[]
repete=[]
while A<=0:
    A= int(input())

    if A <=0:
        repete.append(1)
    else:
        V=1
        while V<=A:
            X= A//V
            Y=A/V
            if X==Y:
                Y=int(Y)
                divisores.append(X)
                V=V+1
            else:
                V=V+1


        b= sum(repete)
        for D in range (b):
            print("VALOR INVÁLIDO")

        divisores.reverse()
        C=len(divisores)
        p=0
        for M in range(C):
            n= divisores[p]
            p=p+1
            print(n,end= " ")
