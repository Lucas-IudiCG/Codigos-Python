


def InicializarGrid():
    V=[]
    for i in range(10):
         linha = []
         for j in range(10):
             linha.append(".")
         V.append(linha)
         
    for i in range(11):
        for j in range(11):
            if i>0 and j>0:
                print(V[i-1][j-1], end="    ")
            elif j==0 and i==0:
                print(" X", end="  ")
            elif i==0:
                print([j-1], end="  ")
            elif j==0:
                print([i-1],end="  ")
    
        print("\n")
    return V

def imprime(V):
    for i in range(11):
        for j in range(11):
            if i>0 and j>0:
                print(V[i-1][j-1], end="    ")
            elif j==0 and i==0:
                print(" X", end="  ")
            elif i==0:
                print([j-1], end="  ")
            elif j==0:
                print([i-1],end="  ")
    
        print("\n")

def ResultadoGrid(attack,grid):
    for i in range(11):
        for j in range(11):
            if i>0 and j>0:
                if attack[i-1][j-1]!=".":
                    print(attack[i-1][j-1], end="    ")
                else:
                    print(grid[i-1][j-1], end="    ")
                    
                    
            elif j==0 and i==0:
                print(" X", end="  ")
            elif i==0:
                print([j-1], end="  ")
            elif j==0:
                print([i-1],end="  ")
    
        print("\n")


def posicionar_porta_avioes(grid, linha, coluna,vertical):
    if vertical==True:
        if grid[linha-2][coluna]!="." or grid[linha-1][coluna]!="." or grid[linha][coluna]!="." or grid[linha+1][coluna]!="." or grid[linha+2][coluna]!=".":
            Confirmacao=False
        else:
            Confirmacao=True
            grid[linha-2][coluna]="P"
            grid[linha-1][coluna]="P"
            grid[linha][coluna]="P"
            grid[linha+1][coluna]="P"
            grid[linha+2][coluna]="P"
        
            
    elif vertical==False:
        if grid[linha][coluna-2]!="." or grid[linha][coluna-1]!="." or grid[linha][coluna]!="." or grid[linha][coluna+1]!="." or grid[linha][coluna+2]!=".":
            Confirmacao=False
        else:
            Confirmacao=True
            grid[linha][coluna-2]="P"
            grid[linha][coluna-1]="P"
            grid[linha][coluna]="P"
            grid[linha][coluna+1]="P"
            grid[linha][coluna+2]="P"
        
    
    

    return Confirmacao

def posicionar_encouracado(grid,linha, coluna,vertical):
    if vertical==True:
        if grid[linha-1][coluna]!="." or grid[linha][coluna]!="." or grid[linha+1][coluna]!="." or grid[linha+2][coluna]!=".":
            Confirmacao=False
        else:
            Confirmacao=True
            grid[linha-1][coluna]="E"
            grid[linha][coluna]="E"
            grid[linha+1][coluna]="E"
            grid[linha+2][coluna]="E"
        
            
    elif vertical==False:
        if grid[linha][coluna-1]!="." or grid[linha][coluna]!="." or grid[linha][coluna+1]!="." or grid[linha][coluna+2]!=".":
            Confirmacao=False
        else:
            Confirmacao=True
            grid[linha][coluna-1]="E"
            grid[linha][coluna]="E"
            grid[linha][coluna+1]="E"
            grid[linha][coluna+2]="E"
        

    return Confirmacao

def posicionar_cruzador(grid,linha, coluna,vertical):
    if vertical==True:
        if grid[linha-1][coluna]!="." or grid[linha][coluna]!="." or grid[linha+1][coluna]!=".":
            Confirmacao=False

        else:
            Confirmacao=True
            grid[linha-1][coluna]="C"
            grid[linha][coluna]="C"
            grid[linha+1][coluna]="C"
        
            
    elif vertical==False:
        if grid[linha][coluna-1]!="." or grid[linha][coluna]!="." or grid[linha][coluna+1]!=".":
            Confirmacao=False
        else:
            Confirmacao=True
            grid[linha][coluna-1]="C"
            grid[linha][coluna]="C"
            grid[linha][coluna+1]="C"
        

    return Confirmacao
    
def posicionar_submarino(grid,linha, coluna,vertical):
    if vertical==True:
        if grid[linha][coluna]!="." or grid[linha+1][coluna]!=".":
            Confirmacao=False
        else:
            Confirmacao=True
            grid[linha][coluna]="S"
            grid[linha+1][coluna]="S"
        
            
    elif vertical==False:
        if grid[linha][coluna]!="." or grid[linha][coluna+1]!=".":
            Confirmacao=False
        else:
            Confirmacao=True
            grid[linha][coluna]="S"
            grid[linha][coluna+1]="S"
        


    return Confirmacao

def Verificar(at,grid):
    A=0
    B=0
    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]!=".":
                A+=1

    for x in range(10):
        for y in range(10):
            if at[x-1][y-1]=="X":
                B+=1
    

    if A==B:
        D=True
        return D
    else:
        D=False
        return D
    
def afundou(at,grid):
    E=XE=0
    P=XP=0
    C=XC=0
    S=XS=0
    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="P":
                P+=1
                
    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="E":
                E+=1

    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="C":
                C+=1
                
    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="S":
                S+=1

    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="S" and at[i-1][j-1]=="X":
                XS+=1
    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="E" and at[i-1][j-1]=="X":
                XE+=1
    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="P" and at[i-1][j-1]=="X":
                XP+=1
    for i in range(10):
        for j in range(10):
            if grid[i-1][j-1]=="C" and at[i-1][j-1]=="X":
                XC+=1

    if E==XE and E!=0:
        print("Voc?? afundou o Encoura??ado")
    if P==XP and P!=0:
        print("Voc?? afundou o Porta Avi??es")
    if S==XS and S!=0:
        print("Voc?? afundou o Submarino")
    elif C==XC and C!=0:
        print("Voc?? afundou o Cruzador")

def atirar(linha,coluna,grid):
    if grid[linha][coluna]==".":
        x="o"
        return x
    else:
        x="X"
        return x

def main():
    print("Atividade Prova N1")
    print("Aluno: Lucas Iudi Corregliano Gallinari")
    print("Turma: 2G")
    print("N??mero de Matricula: 32138628")
    print("")

    Game=False
    C1=False
    C2=False
    C3=False
    C4=False
    grid=InicializarGrid()
    
    print("Modo de Jogo:")
    print("Digite 1 para jogar contra o Computador")
    print("Digite 2 para jogar contra um amigo(ambos precisam estar presente no local)")
    
    Iniciar=False
    while Iniciar==False:
        Inicio=int(input("Digite o Comando: "))
        if Inicio==1:
            Iniciar=True
        elif Inicio==2:
            Iniciar=True
        else:
            print("Comando inv??lido")
            Iniciar=False
    
    if Inicio==1:
        import random
        K=random.randint(0,1)
        if K==0:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(2,7)
                coluna=random.randint(0,9)
                vertical=True
                Confirmacao=posicionar_porta_avioes(grid, linha, coluna,vertical)
        elif K==1:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(0,9)
                coluna=random.randint(2,7)
                vertical=False
                Confirmacao=posicionar_porta_avioes(grid, linha, coluna,vertical)
                
        K=random.randint(0,1)
        if K==0:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(1,7)
                coluna=random.randint(0,9)
                vertical=True
                Confirmacao=posicionar_encouracado(grid, linha, coluna,vertical)
        elif K==1:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(0,9)
                coluna=random.randint(1,7)
                vertical=False
                Confirmacao=posicionar_encouracado(grid, linha, coluna,vertical)

        K=random.randint(0,1)
        if K==0:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(1,8)
                coluna=random.randint(0,9)
                vertical=True
                Confirmacao=posicionar_cruzador(grid, linha, coluna,vertical)
        elif K==1:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(0,9)
                coluna=random.randint(1,8)
                vertical=False
                Confirmacao=posicionar_cruzador(grid, linha, coluna,vertical)

        K=random.randint(0,1)
        if K==0:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(0,8)
                coluna=random.randint(0,9)
                vertical=True
                Confirmacao=posicionar_submarino(grid, linha, coluna,vertical)
        elif K==1:
            Confirmacao=False
            while Confirmacao==False:
                linha=random.randint(0,9)
                coluna=random.randint(0,8)
                vertical=False
                Confirmacao=posicionar_submarino(grid, linha, coluna,vertical)

        attack=InicializarGrid()
        X=0
        D=False
        while X<20 and D==False:
            Confirmacao=False
            while Confirmacao==False:
                Y=20-X
                print("Quantidade de Tiros: ",Y)
                linha=int(input("linha: "))
                coluna=int(input("coluna: "))
                if -1<linha<10 and -1<coluna<10:
                    Confirmacao=True
                else:
                    Confirmacao=False
                    print("Comando Inv??lido")
                
            if attack[linha][coluna]=="o" or attack[linha][coluna]=="X":
                    print("Voc?? j?? escolheu esse espa??o")
                    Confirmacao=False
            else:
                Confirmacao=True
                L=atirar(linha,coluna,grid)
                X+=1
                Y=20-X
                D=Verificar(attack,grid)
                if L== "o":
                    attack[linha][coluna]="o"
                    print("Que Pena, acertou a ??gua")
            
                elif L== "X":
                    attack[linha][coluna]="X"
                    print("Acertou uma Embarca????o")
            imprime(attack)
            afundou(attack,grid)
                
        if D==True:
            print("Jogador Venceu")
            Game=True
        else:
            print("Computador Venceu")
            Game=True
            print("Resultado")
            ResultadoGrid(attack,grid)

    
    elif Inicio==2:
        print("Comandos:")
        print("Digite 1 para posicionar o Porta Avi??es")
        print("Digite 2 para posicionar o Encoura??ado")
        print("Digite 3 para posicionar o Cruzador")
        print("Digite 4 para posicionar o Submarino")
        print("Digite 5 para passar a vez para o Jogador 2")
        while Game==False:
        
            print("Turno do Jogador 1 (Defesa)")
            Menu=int(input("Digite o Comando: "))
            Confirmacao=False
            if Menu==1 and C1==False:
                print("Posicionar Porta Avi??es")
                Confirmacao=False
                while Confirmacao==False:
                    K=int(input("0= vertical, 1= horizontal: "))
                    linha=int(input("linha: "))
                    coluna=int(input("coluna: "))
                    if K==0 and 1<linha<8 and-1<coluna<10:
                        vertical=True
                        Confirmacao=posicionar_porta_avioes(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Porta Avi??es n??o cabe na posi????o selecionado")
                    elif K==1 and -1<linha<10 and 1<coluna<8:
                        vertical=False
                        Confirmacao=posicionar_porta_avioes(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Porta Avi??es n??o cabe na posi????o selecionado")
                    else:
                        print("O Porta Avi??es n??o cabe na posi????o selecionado")
                        K=int(input("0= vertical, 1= horizontal: "))
                        linha=int(input("linha: "))
                        coluna=int(input("coluna: "))
                        if -1<linha<10 and -1<coluna<10:
                            if K==0 and 1<linha<8 and-1<coluna<10:
                                vertical=True
                                Confirmacao=posicionar_porta_avioes(grid, linha, coluna,vertical)
                            elif K==1 and -1<linha<10 and 1<coluna<8:
                                vertical=False
                                Confirmacao=posicionar_porta_avioes(grid, linha, coluna,vertical)
                            print("O Porta Avi??es n??o cabe na posi????o selecionado")

                imprime(grid)
                C1=True
            elif Menu==2 and C2==False:
                print("Posicionar Encoura??ado")
                Confirmacao=False
                while Confirmacao==False:
                    K=int(input("0= vertical, 1= horizontal: "))
                    linha=int(input("linha: "))
                    coluna=int(input("coluna: "))
                    if K==0 and 0<linha<8 and-1<coluna<10:
                        vertical=True
                        Confirmacao=posicionar_encouracado(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Encoura??ado n??o cabe na posi????o selecionado")
                    elif K==1 and -1<linha<10 and 0<coluna<8:
                        vertical=False
                        Confirmacao=posicionar_encouracado(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Encoura??ado n??o cabe na posi????o selecionado")
                    else:
                        print("O Encoura??ado n??o cabe na posi????o selecionado")
                        K=int(input("0= vertical, 1= horizontal: "))
                        linha=int(input("linha: "))
                        coluna=int(input("coluna: "))
                        if -1<linha<10 and -1<coluna<10:
                            if K==0 and 0<linha<8 and-1<coluna<10:
                                vertical=True
                                Confirmacao=posicionar_encouracado(grid, linha, coluna,vertical)
                            elif K==1 and -1<linha<10 and 0<coluna<8:
                                vertical=False
                                Confirmacao=posicionar_encouracado(grid, linha, coluna,vertical)
                            print("O Encoura??ado n??o cabe na posi????o selecionado")
                C2=True
                imprime(grid)
            elif Menu==3 and C3==False:            
                print("Posicionar Cruzador")
                Confirmacao=False
                while Confirmacao==False:
                    K=int(input("0= vertical, 1= horizontal: "))
                    linha=int(input("linha: "))
                    coluna=int(input("coluna: "))
                    if K==0 and 0<linha<9 and -1<coluna<10:
                        vertical=True
                        Confirmacao=posicionar_cruzador(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Cruzador n??o cabe na posi????o selecionado")
                    elif K==1 and -1<linha<10 and 0<coluna<9:
                        vertical=False
                        Confirmacao=posicionar_cruzador(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Cruzador n??o cabe na posi????o selecionado")
                else:
                        print("O Cruzador n??o cabe na posi????o selecionado")
                        K=int(input("0= vertical, 1= horizontal: "))
                        linha=int(input("linha: "))
                        coluna=int(input("coluna: "))
                        if -1<linha<10 and -1<coluna<10:
                            if K==0 and 0<linha<9 and-1<coluna<10:
                                vertical=True
                                Confirmacao=posicionar_cruzador(grid, linha, coluna,vertical)
                            elif K==1 and -1<linha<10 and 0<coluna<9:
                                vertical=False
                                Confirmacao=posicionar_cruzador(grid, linha, coluna,vertical)
                            print("O Cruzador n??o cabe na posi????o selecionado")
                C3=True
                imprime(grid)
            elif Menu==4 and C4==False:
                print("Posicionar Submarino")
                Confirmacao=False
                while Confirmacao==False:
                    K=int(input("0= vertical, 1= horizontal: "))
                    linha=int(input("linha: "))
                    coluna=int(input("coluna: "))
                    if K==0 and -1<linha<9 and -1<coluna<10:
                        vertical=True
                        Confirmacao=posicionar_submarino(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Submarino n??o cabe na posi????o selecionado")
                    elif K==1 and -1<linha<10 and -1<coluna<9:
                        vertical=False
                        Confirmacao=posicionar_submarino(grid, linha, coluna,vertical)
                        if Confirmacao==False:
                            print("O Submarino n??o cabe na posi????o selecionado")
                    else:
                        print("O Submarino n??o cabe na posi????o selecionado")
                        K=int(input("0= vertical, 1= horizontal: "))
                        linha=int(input("linha: "))
                        coluna=int(input("coluna: "))
                        if -1<linha<10 and -1<coluna<10:
                            if K==0 and -1<linha<9 and-1<coluna<10:
                                vertical=True
                                Confirmacao=posicionar_submarino(grid, linha, coluna,vertical)
                            elif K==1 and -1<linha<10 and -1<coluna<9:
                                vertical=False
                                Confirmacao=posicionar_submarino(grid, linha, coluna,vertical)
                            print("O Submarino n??o cabe na posi????o selecionado")
                C4=True
                imprime(grid)
            elif Menu==5:
                for u in range (20):
                    print("")
                print("Turno do Jogador 2 (Ataque)")
                attack=InicializarGrid()
                X=0
                D=False
                while X<20 and D==False:
                    Confirmacao=False
                    while Confirmacao==False:
                        Y=20-X
                        print("Quantidade de Tiros: ",Y)
                        linha=int(input("linha: "))
                        coluna=int(input("coluna: "))
                        if -1<linha<10 and -1<coluna<10:
                            Confirmacao=True
                        elif attack(linha,coluna)=="x" or attack(linha,coluna)=="X":
                            print("Voc?? j?? escolheu esse espa??o")
                            X=X-1
                            
                        else:
                            Confirmacao=False
                            print("Comando Inv??lido")
                    if attack[linha][coluna]=="o" or attack[linha][coluna]=="X":
                        print("Voc?? j?? escolheu esse espa??o")
                        Confirmacao=False
                    else:
                        Confirmacao=True
                        L=atirar(linha,coluna,grid)
                        X+=1
                        Y=20-X
                        D=Verificar(attack,grid)
                        if L== "o":
                            attack[linha][coluna]="o"
                            print("Que Pena, acertou a ??gua")
                        elif L== "X":
                            attack[linha][coluna]="X"
                            print("Acertou uma Embarca????o")
                    afundou(attack,grid)
                    imprime(attack)
                
                if D==True:
                    print("Jogador 2 Ganhou")
                    Game=True
                else:
                    print("Jogador 1 Ganhou")
                    Game=True
                    print("Resultado")
                    ResultadoGrid(attack,grid)

            else:
                print("Comando Inv??lido")


    L=int(input("Finalizar Programa"))
        




main()
