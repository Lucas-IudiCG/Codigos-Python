finalRead = False
string_vazia =""
Letras=[]


Read = open("letra.txt", "r", encoding="utf8")

cont=1
while not finalRead:
    linha= Read.readline(cont)
    if linha == string_vazia:
        finalRead= True
    else:
        Letras.append(linha)

num=len(Letras)
num=num-1

A=0
B=0
C=0
D=0
E=0
F=0
G=0
H=0
I=0
J=0
K=0
L=0
M=0
N=0
O=0
P=0
Q=0
R=0
S=0
T=0
U=0
V=0
W=0
X=0
Y=0
Z=0


while num > -1:
    alfa= str(Letras[num])
    if alfa =="A" or alfa=="Á" or alfa =="Ã":
        A=A+1
        num=num-1
    elif alfa=="E" or alfa =="É":
        E=E+1
        num=num-1
    elif alfa=="I" or alfa=="Í":
        I=I+1
        num=num-1
    elif alfa=="O":
        O=O+1
        num=num-1
    elif alfa=="B":
        B=B+1
        num=num-1
    elif alfa=="C" or alfa=="Ç":
        C=C+1
        num=num-1
    elif alfa=="D":
        D=D+1
        num=num-1
    elif alfa=="F":
        F=F+1
        num=num-1
    elif alfa=="G":
        G=G+1
        num=num-1
    elif alfa=="H":
        H=H+1
        num=num-1
    elif alfa=="J":
        J=J+1
        num=num-1
    elif alfa=="K":
        K=K+1
        num=num-1
    elif alfa=="L":
        L=L+1
        num=num-1
    elif alfa=="M":
        M=M+1
        num=num-1
    elif alfa=="N":
        N=N+1
        num=num-1
    elif alfa=="P":
        P=P+1
        num=num-1
    elif alfa=="Q":
        Q=Q+1
        num=num-1
    elif alfa=="R":
        R=R+1
        num=num-1
    elif alfa=="S":
        S=S+1
        num=num-1
    elif alfa=="T":
        T=T+1
        num=num-1
    elif alfa=="V":
        V=V+1
        num=num-1
    elif alfa=="W":
        W=W+1
        num=num-1
    elif alfa=="X":
        X=X+1
        num=num-1
    elif alfa=="Y":
        Y=Y+1
        num=num-1
    elif alfa=="Z":
        Z=Z+1
        num=num-1    
    else:
        num=num-1

Read.close()

Write= open("resultado.txt","w")

A=str(A)
Write.write("A:" + A + '\n')
B=str(B)
Write.write("B:" + B + '\n')
C=str(C)
Write.write("C:" + C + '\n')
D=str(D)
Write.write("D:" + D + '\n')
E=str(E)
Write.write("E:" + E + '\n')
F=str(F)
Write.write("F:" + F + '\n')
G=str(G)
Write.write("G:" + G + '\n')
H=str(H)
Write.write("H:" + H + '\n')
I=str(I)
Write.write("I:" + I + '\n')
J=str(J)
Write.write("J:" + J + '\n')
K=str(K)
Write.write("K:" + K + '\n')
L=str(L)
Write.write("L:" + L + '\n')
M=str(M)
Write.write("M:" + M + '\n')
N=str(N)
Write.write("N:" + N + '\n')
O=str(O)
Write.write("O:" + O + '\n')
P=str(P)
Write.write("P:" + P + '\n')
Q=str(Q)
Write.write("Q:" + Q + '\n')
R=str(R)
Write.write("R:" + R + '\n')
S=str(S)
Write.write("S:" + S + '\n')
T=str(T)
Write.write("T:" + T + '\n')
U=str(U)
Write.write("U:" + U + '\n')
V=str(V)
Write.write("V:" + V + '\n')
W=str(W)
Write.write("W:" + W + '\n')
X=str(X)
Write.write("X:" + X + '\n')
Y=str(Y)
Write.write("Y:" + Y + '\n')
Z=str(Z)
Write.write("Z:" + Z + '\n')

Write.close()
