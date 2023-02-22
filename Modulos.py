
def funcao(S):
    Result=0
    while S> 0:
        num1 = S
        num2= num1**2
        Result= (num1/num2) + Result
        S=S-1
    return Result

        

def EhPrimo(N):
    X=N
    V=0
    while X>=1:
        Z= (N/X)- (N//X)
        X=X-1
        if Z== "0":
            V=V+1

    if V >2:
        print("Não é primo")
        return 
    else:
        print("é primo")

def multiplica(a,b):
    Soma = 0
    while 0 < b:
        b= b -1
        Soma =Soma+a
    return Soma



def potencia(c,d):
    mult = c
    while 0 < d:
        d= d -1
        mult =mult*c
    return mult




def main():

    S= int(input())
    print(S)
    print(funcao(S))

    N= int(input())
    print(N)
    EhPrimo(N)

    a= int(input())
    print(a)
    b= int(input())
    print(b)
    print (multiplica(a,b))
    
    c= int(input())
    print(c)
    d= int(input())
    print(d)
    print (potencia(c,d))

    


main()
