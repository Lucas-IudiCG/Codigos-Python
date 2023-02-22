#Projeto Jogo da Velha :(


def Initialize():
    V=[]
    for i in range(3):
         linha = []
         for j in range(3):
             linha.append("*")
         V.append(linha)

    for i in range(3):
        for j in range(3):
            print(V[i][j], end="")
            if j<2:
                print("/", end="")
        print("\n")
    return V

def step(M,lin,col,gamer):
    Final=True
    if gamer==1:
        if M[lin][col]=="*":
            M[lin][col]="O"
            print("Comando Aceito")
            Final=True
            return Final
        elif M[lin][col]=="O":
            print("Comando Inválido")
            print("Você já escolheu esse espaço")
            Final=False
            return Final
        elif M[lin][col]=="X":
            print("Comando Inválido")
            print("O seu Oponente já escolheu esse espaço")
            Final=False
            return Final
    elif gamer==2:
        if M[lin][col]=="*":
            M[lin][col]="X"
            print("Comando Aceito")
            Final=True
            return Final
        elif M[lin][col]=="X":
            print("Comando Inválido")
            print("O seu Oponente já escolheu esse espaço")
            Final=False
            return Final
        elif M[lin][col]=="O":
            print("Comando Inválido")
            print("Você já escolheu esse espaço")
            Final=False
            return Final

def status(M):
    D=0
    for i in range(3):
         for j in range(3):
             if M[i][j]=="*":
                 D+=1

    if D>0:
        if M[0][0]==M[1][1]==M[2][2]=="X":
            D=2
            return D
        elif M[0][0]==M[1][1]==M[2][2]=="O":
            D=1
            return D
        elif M[0][0]==M[0][1]==M[0][2]=="X":
            D=2
            return D
    else:
        print("EMPATE")
        return D


def Imprime (M):
    for i in range(3):
        for j in range(3):
            print(M[i][j], end="")
            if j<2:
                print("/", end="")
        print("\n")


def main():
    M= Initialize()
    Cont=1
    veri=3
    J1=str(input("Digite seu nome Jogador N1(O): "))
    J2=str(input("Digite seu nome Jogador N2(X): "))
    while veri==3:
        
        F=False
        if Cont==1 and veri==3:
            print("Turno de",J1)
            lin=int(input("Digite a linha: "))
            lin=lin-1
            col=int(input("Digite a coluna: "))
            col=col-1
            
            while F==False:
                F=step(M,lin,col,Cont)
                print(F)
                if F==False:
                    lin=int(input("Digite a linha: "))
                    lin=lin-1
                    col=int(input("Digite a coluna: "))
                    col=col-1
                Imprime(M)
            Cont=2
            F=False
        veri=status(M)   
        if Cont==2 and veri==3:
            print("Turno de",J2)
            lin=int(input("Digite a linha: "))
            lin=lin-1
            col=int(input("Digite a coluna: "))
            col=col-1
                
            while F==False:
                F=step(M,lin,col,Cont)
                print(F)
                if F==False:
                    lin=int(input("Digite a linha: "))
                    lin=lin-1
                    col=int(input("Digite a coluna: "))
                    col=col-1
                Imprime(M)
            F=False
            Cont=1
            
        




main()
