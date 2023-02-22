def EhPrimo(num1,num2):
    x= num2
    while num1 < num2:
        div= num2/x
        trunc= num2//x
        x=num2-1
        if div == trunc:
            print(num2)


def main():

    num1= int(input())
    print(num1)
    num2= int(input())
    print(num2)
    print (EhPrimo(num1,num2))


    




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

    a= int(input())
    print(a)
    b= int(input())
    print(b)
    print (multiplica(a,b))
    
    c= int(input())
    print(c)
    d= int(input())
    print(d)
    print (potencial(c,d))

    


main()
