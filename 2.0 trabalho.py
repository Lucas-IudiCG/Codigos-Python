#Entrega do Trabalho 1- Algoritmos e Programação II
#Eu: Lucas Iudi Corregliano Gallinari

#declaro que
#todas as respostas são fruto de nosso próprio trabalho,
#não copiamos respostas de colegas externos à equipe,
#não disponibilizamos nossas respostas para colegas externos ao grupo e
#não realizamos quaisquer outras atividades desonestas para nos beneficiar 
#ou prejudicar outros.


    

# Na função Polinomio o usuario poderá selecionar o grau no polinomio, bem como os seus coeficientes.
def Polinomio():
    size=0
    while size<=0:
        size = int(input("Grau do polinómio: "))
        A=[0]*(size+1)
        if size>0:
            A=[0]*(size+1)
            for i in range (size+1):
                A[i]=float(input("qual seria o coeficiênte? "))
                if A[i]<0:
                    A[i]=-(A[i])

        else:
            print("Comando Invalido: o Número digitado não pertence aos Números Naturais")
    return A

# Na função Sinal è feita para designar o Sinal de cada Digito.
def Sinal(A):
    H=len(A)
    S=[0]*H
    for I in range (H):
        Teste= 1
        S[I]=int(input("Digite 0 se for Positivo ,ou 1 para Negativo: "))
        if S[I]==1 or S[I]==0:
            print("Comando Aceito")
            
        else:
            while Teste==1:
                print("Comando Inválido")
                S[I]=int(input("Digite 0 se for Positivo ,ou 1 para Negativo: "))
                if S[I]==1 or S[I]==0:
                    Teste=0
                else:
                    Teste=1
                
    print(S)       
    return S

# ImprimePoli pega duas variaveis um representando os números e outras o sinal para "Imprimir", o polinomio 
def imprimePoli(A,S):
    H=len(A)-1
    print("P(x)=", end=" ")
    for y in range(len(A)):
        if H== 0:
            if S[y]==1:
                print("-",A[y])
            elif S[y]==0:
                print("+",A[y])
        elif H==1:
            H=H-1
            if S[y]==1:
                print("-",A[y],"X", end=" ")
            elif S[y]==0:
                print("+",A[y],"X", end=" ")
            
            

        else:
            if S[y]==1:
                print("-",A[y],"X^",H, end=" ")
            elif S[y]==0:
                print("+",A[y],"X^",H, end=" ")
            H=H-1
            
# Essa função realiza a substituição da variavel X do Polinomio, e calcula o seu resultado.
def Resulcao(A,S):
    resp=0
    Z=0
    H=len(A)-1
    X=float(input("Qual seria o Valor de X: "))
    Y=A[1]
    equa=Y*(X**H)
    if S[0]==0:
        Z=equa
        H=H-1
    elif S[0]==1:
        Z=-equa
        H=H-1
        
    for R in range (H):
        Y=A[R+1]
        equa=Y*(X**H)
        if S[R+1]==0:
            Z=equa+Z
            H=H-1

        elif S[R+1]==1:
            Z1=-equa
            Z=Z1+Z
            H=H-1
            
            

    H=len(A)-1
    if S[H]==0:
        Z=Z+A[H]
    elif S[H]==1:
        Z=Z-A[H]

        
    return Z



# A função transição regasta os valores do sinal(S)associa ao valor de cada coeficiente do polinomio(A) gerando os valores positivos e negativos
def  Transicao (A,S):
    H=len(A)
    H=H
    V=[0]*H
    for G in range(H):
        if S[G]==1:
            V[G]=int(-(A[G]))
        else:
            V[G]= int(A[G])
    return V


#Essa função realiza a soma dos 2 polinomios salvos, decteta qual deles é o maior calcula a sua diferença, e apartir deste cálculo, gera dois vetores auxiliares e soma seus respectivos coefiecientes de acordo com o seu grau.
def Soma(B,C):
    HB=len(B)
    HC=len(C)
    H1=0
    if HB>=HC:
        H1=HB
        HD=HB-HC
        D=[0]*HB
        E=[0]*HB
        F=[0]*HB
        for V in range(HC):
            F[V+HD]=C[V]

        for G in range(HB):
            E[G]=B[V]

    elif HC>HB:
        H1=HC
        HD=HC-HB
        D=[0]*HC
        E=[0]*HC
        F=[0]*HC
        for V in range(HB):
            F[V+HD]=B[V]

        for G in range(HC):
            E[G]=C[G]

    for I in range(H1):
        Soma1=E[I]+F[I]
        D[I]=Soma1

    K=H1-1
    for J in range (H1):
        if D[J]<0:
            if K==0:
                print(D[J])
                K=K-1
            elif K==1:
                print(D[J],"X",end=" ")
                K=K-1
            else:
                print(D[J],"X^",K,end=" ")
                K=K-1
                
                
        elif D[J]==0:
            print(" ")
            K=K-1
            
        else:
            if K==0:
                print("+",D[J])
                K=K-1
            elif K==1:
                print("+",D[J],"X",end=" ")
                K=K-1
            else:
                print("+",D[J],"X^",K,end=" ")
                K=K-1


    return D

#A função principal funciona como o menu ,e base na qual fara com que multiplas funções se cordenem a ponto de resolver as perguntas
def main():
    H=1
    print("Menu")
    print("Digite 1 caso queira Salvar o polinómio(1)")
    print("Digite 2 caso queira Salvar o polinómio(2)")
    print("Digite 3 caso queira Resolver um polinómio")
    print("Digite 4 caso queira imprimir os polinómios")
    print("Digite 5 caso queira Somar os polinómios")
    print("Digite 0 caso queira rfinalizar o programa")
    while H!=0:
        Menu=input("Comando: ")
        if Menu=="1":
            uno=1
            while uno==1:
                num1=Polinomio()
                Sig1=Sinal(num1)
                imprimePoli(num1,Sig1)
                print("Esse Polinómio está correto,digite(S) ou (N) ?")
                conf=str(input(""))
                if conf=="Sim" or conf=="S" or conf=="sim" or conf =="s" or conf=="SIM" or conf =="S" or conf =="(S)":
                    uno=0
                else:
                    print("O Polinómio foi resetado")
                    uno=1

        elif Menu=="2":
            dos=1
            while dos==1:
                num2=Polinomio()
                Sig2=Sinal(num2)
                imprimePoli(num2,Sig2)
                print("Esse Polinómio está correto?")
                conf=str(input(""))
                if conf=="Sim" or conf=="S" or conf=="sim" or conf =="s" or conf=="SIM" or conf =="S" or conf =="(S)":
                    dos=0
                else:
                    print("O Polinómio foi resetado")
                    dos=1

        elif Menu=="3":
            tres=1
            while tres== 1:
                opc=int(input("Qual polinómio será resolvido (1) ou (2): "))
                if opc==1:
                    tres=0
                    print(Resulcao(num1,Sig1))
                elif opc==2:
                    tres=0
                    print(Resulcao(num2,Sig2))
                else:
                    print("Comando Invalido")
                    tres=1

        elif Menu=="4":
            print("Digite 1 se deseja ver o polinómio 1")
            print("Digite 2 se deseja ver o polinómio 2")
            print("Digite 3 se deseja ver ambos os polinómio")
            qua=1
            while qua==1:
                imp=int(input("Comando: "))
                if imp==1:
                    imprimePoli(num1,Sig1)
                    qua=0
                elif imp==2:
                    imprimePoli(num2,Sig2)
                    qua=0
                elif imp==3:
                    imprimePoli(num1,Sig1)
                    imprimePoli(num2,Sig2)
                    qua=0
                else:
                    print("Comando inválido")

        elif Menu=="5":
            Sum1=Transicao(num1,Sig1)
            print(Sum1)
            Sum2=Transicao(num2,Sig2)
            print(Sum2)
            Soma(Sum1,Sum2)


        elif Menu=="0":
            print("Programa Finalizado!")
            H=0

        else:
            print("Comando Inválido")
            print("Menu")
            print("Digite 1 caso queira Salvar o polinómio(1)")
            print("Digite 2 caso queira Salvar o polinómio(2)")
            print("Digite 3 caso queira Resolver um polinómio")
            print("Digite 4 caso queira imprimir os polinómios")
            print("Digite 5 caso queira Somar os polinómios")
            print("Digite 0 caso queira rfinalizar o programa")

            


        





main()
