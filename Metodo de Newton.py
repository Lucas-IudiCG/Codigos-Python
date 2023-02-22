#Metodo de Newton

def Newton(f,p,epsilion):
    x=100
    j=0
    while(x>epsilion):
        Fx=0
        FLX=0
        p1=0
        for i in range(len(f)):
            if(i%2==0):
                if((f[i+1]-1)!=0):
                    Fx+=f[i]*(p**f[i+1])
                else:
                    Fx+=f[i]
                      
        for i in range(len(f)):
            if(i%2==0):
                if((f[i+1]-1)!=0):
                    FLX+=(f[i]*f[i+1])*(p**(f[i+1]-1))
        p1=p-(Fx/FLX)
        j+=1
        x=p1-p
        p=p1
    print("Iterações: ",j)
    return p

def main():
    funcao=[]
    n1=int(input("Quantos elementos tem na função: "))
    for i in range(n1*2):
        if(i%2==0):
            n2=int(input("digite um numero: "))
        elif(i%2==1):
            n2=int(input("digite o seu Expoente: "))
        funcao.append(n2)
    p0=float(input("p0: "))
    epsilon=float(input("(e): "))
    print("Raiz: ",Newton(funcao,p0,epsilon))

    
main()
