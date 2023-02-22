# Lista de Exercicios de Lista

N=2
Notas=[]
for i in range (5):
    N= float(input("Nota do Aluno: "))
    if 0<= N or N >=0:
        Notas.append(N)
        print(Notas)
    else:
        print("Valor Invalido")


S=sum(Notas)
S1=S/5
print("media: "S1)

m=min(Notas)
M=max(Notas)
print(M,m)
