def criaMatriz(X,Y):
     M = []
     for i in range(X):
         linha = []
         for j in range(Y):
             linha.append(0)
         M.append(linha)

     return M

def Imprime(I):
     for i in range(len(I)):
        for j in range(len(I[0])):
            if (I[i][j]>=0 and j>0):
                print("+",I[i][j],"x",j+1, end=" ")
            else:
                print(I[i][j],"x",j+1, end=" ")
        print("\n")

def main():
    tol=float(input("tolerancia: "))
    num2=int(input("numero de variaveis: "))
    num1=int(input("numero de equações: "))
    num2+=1
    vet1=criaMatriz(num1,num2)
    for A in range(num1):
        for B in range(num2):
            print("funcão de ",A+1,"|",B+1,": ")
            Var=int(input())
            vet1[A][B]=Var
    Imprime(vet1)
    return 0



main()
