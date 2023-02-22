# Exercicio 2 Extra

finalRead = False
string_vazia =""
ID=[]
Money =[]


Read = open("salarios.csv", "r")


while not finalRead:
    linha= Read.readline()
    if linha == string_vazia:
        finalRead= True
    else:
        
        A =linha.rstrip()
        x= A.split(":")[0]
        ID.append(x)
        x1= A.split(":")[1]
        Money.append(x1)

print(ID)
print(Money)

Read.close()

W = open('salarios_5000.csv', 'w')

A=len(ID)
A=A-1

X=0

while A >-1:
    if float(Money[X]) >= 5000.00:
        W.write(ID[X] + ':' + Money[X] + '\n')
        A=A-1
        X=X+1
    else:
        A=A-1
        X=X+1
        




W.close()

