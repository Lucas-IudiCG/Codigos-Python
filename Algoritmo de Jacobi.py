def gerar_matriz (n_linhas, n_colunas):
    matriz = []
    for l in range(n_linhas):
        linha = []
        for c in range(n_colunas):
            numero = float(input(" digite o numero que ficara armazenado {},{} :".format(l+1, c+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def Jacobi1(M,n1,n2):
    linha = []
    for l in range(n1):
        num1=0
        for c in range(n2):
            if (num1<M[l][c]):
                num1=M[l][c]
                C=c
                L=l
        linha.append(num1)
        M[L][C]=0
    for l in range(n1):
        for c in range(n2):
            M[l][c]=M[l][c]/linha[l]
    return M, linha


def Conta(vet,MAX,M,n1,n2):
    Soma=0
    Resultado=[]
    for l in range(n1):
        Soma=0
        for c in range(n2):
            M[l][c]=M[l][c]*vet[c]
            Soma=Soma+M[l][c]
        Resultado.append(Soma)
    print(Resultado)
    Resultado.append(1)
    return Resultado

def verificar(V1,V2,n):
    Numerador=0
    Denominador=0
    for l in range(n):
        if(Numerador<abs(V2[l]-V1[l])):
            Numerador=abs(V2[l]-V1[l])
        elif(Denominador<abs(V2[l])):
            Denominador=abs(V2[l])
    Tol=Numerador/Denominador
    print(Tol)
    return Tol

def main():
    n1=int(input("Equações: "))
    n2=int(input("Variaveis: "))
    Tolerancia=float(input("Tolerancia: "))
    M=gerar_matriz(n1,n2+1)
    V1,MAX=Jacobi1(M,n1,n2+1)
    variaveis=[(2/3),-1/3,(3),1]
    x=1
    i=0
    v2=[]
    while(x>Tolerancia):
        v2=Conta(variaveis,MAX,V1,n1,n2+1)
        x=verificar(variaveis,v2,n2)
        i+=1
        variaveis=v2
    print("iteracoes realizadas: ",i)
    
    return 1
    
main()

