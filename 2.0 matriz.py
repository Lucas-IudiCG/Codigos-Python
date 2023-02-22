import random

def criaMatriz(X,Y):
     M = []
     for i in range(X):
         linha = []
         for j in range(Y):
             linha.append(random.randint(1,100))
         M.append(linha)

     return M            


def verificaMaior(M):
    K=0
    for i in range (len(M)):
        for j in range (len(M[0])):
            if M[i][j]>=K:
                K=int(M[i][j])
    return K

def quadrado(M):
    D=[]
    K=0
    for i in range (len(M)):
        linha = []
        for j in range (len(M[0])):
            if i==j:
                K=K+M[i][j]
                linha.append(int(M[i][j]))
        D.append(linha)
    print("É uma Matriz quadrado e sua diagonal é igual a: ",D)            
    return K

def quadradoInverso(M):
    D=[]
    K=0
    for i in range (len(M)):
        linha = []
        for j in range (len(M[0])):
            if i+j==len(M)-1:
                K=K+M[i][j]
                linha.append(int(M[i][j]))
        D.append(linha)
    print("É uma Matriz quadrado e sua diagonal é igual a: ",D)            
    return K


def main():
    X= int(input("Digite o Números de Linhas: "))
    Y= int(input("Digite o Números de Colunas: "))
    mat=criaMatriz(X,Y)
    print("[M]=")
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print("\n")
    print("O maior elemento é: ", verificaMaior(mat))
    if X==Y:
        C=quadrado(mat)
        print("Soma da diagonal igual a: ",C)
        D=quadradoInverso(mat)
        print("E a sua diagonal inversa é igual a: ",D)
        

    
        
    
        




main()
    
    
