import random
M=[]
for i in range(40):
    linha=[]
    for j in range(40):
        linha.append(random.randint(0,5))
    M.append(linha)



Produtos=[]
for c in range(40):
    linha=[]
    for d in range(40):
        linha.append("")
    Produtos.append(linha)
        
for a in range(40):
    for b in range(40):
        T=M[a][b]
        if T==0:
            Produtos[a][b]="Vazio"
        elif T==1:
            Produtos[a][b]="Xampu"
        elif T==2:
            Produtos[a][b]="Condicionador"
        elif T==3:
            Produtos[a][b]="Hidratante"
        elif T==4:
            Produtos[a][b]="Tintura"
        elif T==5:
            Produtos[a][b]="Demaquilante"
            
print(Produtos)
X0=0
X1=0
X2=0
X3=0
X4=0
X5=0
for x in range(40):
    for y in range(40):
        T=M[x][y]
        if T==0:
            X0+=1
        elif T==1:
            X1+=1
        elif T==2:
            X2+=1
        elif T==3:
            X3+=1
        elif T==4:
            X4+=1
        elif T==5:
            X5+=1

print("quantidade de Xampu",X2)
print("quantidade de Condicionador",X3)
print("quantidade de Hidrante",X3)
print("quantidade de Tintura",X4)
print("quantidade de Demaquilante",X5)
print("quantidade de Vazio",X0)

