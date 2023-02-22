finalRead = False
string_vazia =""
Time1 =[]
Time2 = []
Gols1 = []
Gols2 = []
Vitorias = []

Read = open("resultados_jogos.txt", "r")


print("Resultados:")


while not finalRead:
    linha= Read.readline()
    if linha == string_vazia:
        finalRead= True
    else:
        
        time =linha.rstrip()
        x1= time.split(":")[0]
        x2= time.split(":")[1]
        x3= time.split(":")[2]
        x4= time.split(":")[3]
        Time1.append(x1)
        Gols1.append(x2)
        Time2.append(x3)
        Gols2.append(x4)
        


Read.close()

A=len(Time1)
A=A-1

X=0

while A >-1:
    B1=int(Gols1[X])
    B2=int(Gols2[X])
    if B1>B2:
        Vitorias.append(Time1[X])
        A=A-1
        X=X+1
    if B2>B1:
        Vitorias.append(Time2[X])
        A=A-1
        X=X+1
    if B2 == B1:
        A=A-1
        X=X+1


print(Vitorias)

A=len(Vitorias)
A=A-1
print(A)
C=0
G=0
P=0
S=0
X=0
while A >-1:
    if Vitorias[X]== "Corinthians":
        X=X+1
        C=C+1
        A=A-1
    elif Vitorias[X]== "Guarani":
        G=G+1
        X=X+1
        A=A-1
    elif Vitorias[X]== "Palmeiras":
        P=P+1
        X=X+1
        A=A-1
    elif Vitorias[X]== "São Paulo":
        S=S+1
        X=X+1
        A=A-1




print("CORINTHIANS: ",C, "VITÓRIAS")
print("GUARANI: ",G, "VITÓRIAS")
print("PALMEIRAS: ",P, "VITÓRIAS")
print("SÃO PAULO: ",S, "VITÓRIAS")

V=str(input("Pressione algum botão para finalizar o Programa: A"))
