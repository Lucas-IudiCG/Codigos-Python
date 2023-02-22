
def Fila(x):
    Caminhoneiros=[]
    for a in range (x):
        print(a+1,end=" ")
        txt=str(input("Digite o nome dos caminhoneiros:"))
        Caminhoneiros.append(txt)
    return Caminhoneiros


def estaVazia(Total):
    if Total==0:
        return True
    else:
        return False


def estaCheia(Total):
    if Total >=10:
        return True
    else:
        return False
    
def enfilerar(V):
    if estaCheia(len(V))==False:
        X=str(input("Digite o nome dos caminhoneiros:"))
        V.append(X)
    else:
        print("Fila Cheia")


def main():
    x=int(input("Vamos la: "))
    V=Fila(x)
    Total=len(V)
    while estaCheia(Total)==False:
        enfilerar(Total,V)
    


main()
