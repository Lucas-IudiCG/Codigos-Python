#Exercício 1

finalRead = False
string_vazia =""
Lista=[]

print("Exercício1")

Read = open("times.txt", "r")


print("Times que Participarão deste campeonato:")

while not finalRead:
    linha= Read.readline()
    if linha == string_vazia:
        finalRead= True
    else:
        time =linha.rstrip()
        Lista.append(time)


Alfabetica = sorted(Lista)

Read.close()


print(Alfabetica)

A1=str(input("Precione qualquer tecla para finalizar a primeira parte do programa: "))

# Exercicio 2


N= len(Alfabetica)

Read = open('times.txt', 'r')


X=N-1
print("Exercício 2")
print("Os Jogos Serão:")



while X > -1:
    print(Alfabetica[X], " X ", Alfabetica[X-1])
    print(Alfabetica[X], " X ", Alfabetica[X-2])
    print(Alfabetica[X], " X ", Alfabetica[X-3])
    X=X-1



A2=str(input("Precione qualquer tecla para finalizar a programa: "))

