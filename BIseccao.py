#Biseccao


def Biseccao(f,a,b,epsilion):
    x=100
    i=0
    while(x>epsilion):

        SomaA=0
        for i in range(len(f)):
            if(i%2==0):
                SomaA+=(f[i]*(a**f[i+1]))
        SomaB=0
        for i in range(len(f)):
            if(i%2==0):
               SomaB+=(f[i]*(b**f[i+1]))
        m=(a+b)/2
        SomaF=0
        for i in range(len(f)):
            if(i%2==0):
               SomaF+=(f[i]*(m**f[i+1]))
        if(SomaF*SomaA<0):
            b=m
        elif(SomaF*SomaB<0):
            a=m
        x=SomaF
        i+=1
    print("Iterações: ",i)
    return (a+b)/2





def main():
    funcao=[]
    n1=int(input("Quantos elementos tem na função: "))
    for i in range(n1*2):
        if(i%2==0):
            n2=int(input("digite um numero: "))
        elif(i%2==1):
            n2=int(input("digite o seu Expoente: "))
        funcao.append(n2)
    a=float(input("(a): "))
    b=float(input("(b): "))
    epsilon=float(input("(e): "))
    print("Raiz: ",Biseccao(funcao,a,b,epsilon))

    
main()
