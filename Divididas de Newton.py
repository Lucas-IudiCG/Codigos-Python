#Diferenças Divididas de Newton

def DivNewton(x,funcao,n):
    Resultado=[0]*n
    Auxiliar=[0]*n
    j=1
    for i in range(n):
        Auxiliar[i]=funcao[i]
    while(j<n):
        for i in range(n-j):
            if(Auxiliar[i+1]-Auxiliar[i]==0 or x[i+j]-x[i]==0):
                Resultado[i]=0
            else:
                Resultado[i]=(Auxiliar[i+1]-Auxiliar[i])/(x[i+j]-x[i])
        for i in range(n):
            Auxiliar[i]=Resultado[i]
            Resultado[i]=0
            
            
        j+=1
    print("Divisões: ",j-1)
    return Auxiliar[0]
        
   
def main():
    x=[]
    funcao=[]
    n=int(input("Quantos elementos tem na tabela: "))
    for i in range(n):
        n1=float(input("digite X: "))
        n2=float(input("digite F(X): "))
        x.append(n1)
        funcao.append(n2)
    print(DivNewton(x,funcao,n))
    

    
main()
