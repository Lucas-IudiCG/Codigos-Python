# Contagem 50 até 100

num = 50

while num <=100:
    print(num, end =" ")
    num=num+1

#Contagem Regressiva

Num2 = 10


while Num2 >= 0:

    if Num2 != 0:
        print(Num2, end = ",")
        Num2= Num2-1
        


    else:
        print( "0 e FOGO")
        Num2 = Num2 -1

# pares até y

Y = int(input("Digite um numero: "))
X=0

while X<=Y:
    print(X, end = " ")
    X=X+2


# Pares de 0 até Y(Com IF)

Y = int(input( "Digite um numero: "))
X=0

while X!=Y:
    
    if X<Y:
        print(X, end = " ")
        X=X+2

    else:
        print(X, end = " ")
        X=X-2
