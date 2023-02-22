print("Atividade Prova N1")
print("Aluno: Lucas Iudi Corregliano Gallinari")
print("Turma: 2G")
print("Número de Matricula: 32138628")


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

def posicionar_porta_avioes(grid, linha, coluna,vertical):
    if vertical==False:
        grid[linha-2][coluna]="P"
        grid[linha-1][coluna]="P"
        grid[linha][coluna]="P"
        grid[linha+1][coluna]="P"
        grid[linha+2][coluna]="P"
        
            
    elif vertical==True:
        grid[linha][coluna-2]="P"
        grid[linha][coluna-1]="P"
        grid[linha][coluna]="P"
        grid[linha][coluna+1]="P"
        grid[linha][coluna+2]="P"
        
    for i in range(11):
        for j in range(11):
            if i>0 and j>0:
                print(grid[i-1][j-1], end="    ")
            elif j==0 and i==0:
                print(" X", end="  ")
            elif i==0:
                print([j-1], end="  ")
            elif j==0:
                print([i-1],end="  ")
    
        print("\n")


grid=InicializarGrid()
print("Posicionar Porta Aviões")
linha=int(input("linha: "))
coluna=int(input("coluna: "))
if 1<linha<8 and 1<coluna<8:
    K=int(input("1= vertical, 0= horizontal: "))
    if K==0:
        vertical=True
    elif K==1:
        vertical=False
    posicionar_porta_avioes(grid, linha, coluna,vertical)
else:
    while linha<2 or linha>8 or coluna<2 or coluna>8:
        print("O Porta Aviões não cabe na posição selecionado")
        linha=int(input("linha: "))
        coluna=int(input("coluna: "))
        if 1<linha<8 and 1<coluna<8:
            K=int(input("1= vertical, 0= horizontal: "))
            if K==0:
                vertical=True
            elif K==1:
                vertical=False
            posicionar_porta_avioes(grid, linha, coluna,vertical)
            
