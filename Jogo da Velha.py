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
        elif M[lin][col]=="O":
            print("Comando Inválido")
            print("O seu Oponente já escolheu esse espaço")
            Final=False
            return Final
        elif M[lin][col]=="X":
            print("Comando Inválido")
            print("Você já escolheu esse espaço")
            Final=False
            return Final

def status(M):
    if M[0][0]==M[1][1]==M[2][2]=="X":
        D=2
        return D
    elif M[0][2]==M[1][1]==M[2][0]=="X":
        D=2
        return D
    
    elif M[0][0]==M[0][1]==M[0][2]=="X":
        D=2
        return D
    elif M[1][0]==M[1][1]==M[1][2]=="X":
        D=2
        return D
    elif M[2][0]==M[1][1]==M[0][2]=="X":
        D=2
        return D
    
    elif M[0][0]==M[1][0]==M[2][0]=="X":
        D=2
        return D
    elif M[0][1]==M[1][1]==M[2][1]=="X":
        D=2
        return D
    elif M[0][2]==M[1][2]==M[2][2]=="X":
        D=2
        return D

    elif M[0][0]==M[1][1]==M[2][2]=="O":
        D=1
        return D
    elif M[0][2]==M[1][1]==M[2][0]=="O":
        D=1
        return D
    
    elif M[0][0]==M[0][1]==M[0][2]=="O":
        D=1
        return D
    elif M[1][0]==M[1][1]==M[1][2]=="O":
        D=1
        return D
    elif M[2][0]==M[2][1]==M[2][2]=="O":
        D=1
        return D

    elif M[0][0]==M[1][0]==M[2][0]=="O":
        D=1
        return D
    elif M[0][1]==M[1][1]==M[2][1]=="O":
        D=1
        return D
    elif M[0][2]==M[1][2]==M[2][2]=="O":
        D=1
        return D
    else:
        D=0
        for i in range(3):
            for j in range(3):
                if M[i][j]=="*":
                    D+=1
        if D>0:
            D=3
            return D
        else:
            D=0
            return D


def Imprime (M):
    for i in range(3):
        for j in range(3):
            print(M[i][j], end="")
            if j<2:
                print("/", end="")
        print("\n")

def game():
    Write=open("Resultados.txt","w")

    return Write

def main():
    M= Initialize()
    Jogador=1
    K=0
    Cont=1
    veri=3
    J1=str(input("Digite seu nome Jogador N1(O): "))
    J2=str(input("Digite seu nome Jogador N2(X): "))
    while veri==3:
        F=False
        Cont=1
        if Jogador==1 and veri==3:
            print("Turno de",J1)
            lin=-1
            col=-1
            while F==False or lin<0 or lin>3 or col<0 or col>3:
                if lin<0 or lin>3 or col<0 or col>3:
                    print("Escolha uma Coordenada")
                    lin=int(input("Digite a linha: "))
                    lin=lin-1
                    col=int(input("Digite a coluna: "))
                    col=col-1
                    if lin<0 or lin>3 or col<0 or col>3:
                        print ("Comando Inválido")
                elif F==False:
                    F=step(M,lin,col,Cont)
                    if F==False:
                        lin=int(input("Digite a linha: "))
                        lin=lin-1
                        col=int(input("Digite a coluna: "))
                        col=col-1
            Imprime(M)
            veri=status(M)
            Cont+=1
            K+=1
            F=False
            Jogador=2

            
        if Jogador==2 and veri==3:
            print("Turno de",J2)
            lin=-1
            col=-1
            while F==False or lin<0 or lin>3 or col<0 or col>3:
                if lin<0 or lin>3 or col<0 or col>3:
                    print("Escolha uma Coordenada")
                    lin=int(input("Digite a linha: "))
                    lin=lin-1
                    col=int(input("Digite a coluna: "))
                    col=col-1
                    if lin<0 or lin>3 or col<0 or col>3:
                        print ("Comando Inválido")
                elif F==False:
                    F=step(M,lin,col,Cont)
                    if F==False:
                        lin=int(input("Digite a linha: "))
                        lin=lin-1
                        col=int(input("Digite a coluna: "))
                        col=col-1
            Imprime(M)
            veri=status(M)
            F=False
            Cont+=1
            K+=1
            Jogador=1

            
    if veri==2:
        print("Vitoria de Jogador N2(X)")
        print(J2)
        W.write(str(K)+"; Jogador N2 (X): "+ str(J2))
        W.write("\n")

    elif veri==1:
        print("Vitoria de Jogador N1(O)")
        print(J1)
        W.write(str(K)+"; Jogador N1 (O): "+ str(J1))
        W.write("\n")


    elif veri==0:
        print("EMPATE")
        W.write(str(K)+"; EMPATE")
        W.write("\n")
        
    test=False
    while test==False:
        print("Jogador novamente?")
        Jog=str(input("Sim(S) ou Não(N)"))
        if Jog=="S" or Jog=="s" or Jog== "Sim" or Jog=="sim":
            print("Jogo recomeçado")
            test=True
            main()
        elif Jog=="N" or Jog=="n" or Jog== "Não" or Jog=="não" or Jog=="nao" or Jog=="Nao":
            print("Jogo Finalizado")
            W.close()
            test=True
            
        else:
            test=False
            print("Comando Inválido")
        
            



W=game()
main()
