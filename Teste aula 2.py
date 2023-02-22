n1= int(input ('numero 1: '))
n2= float(input ('numero 2: '))
divisão = n1/n2
quociente = n1//n2
resto = n1%n2
multiplicação = n1*n2
exponencial = n1**n2
media = (n1+n2)/2
print ('divisão', divisão)
print("divisão truncada", quociente)
print ("resto", resto)
print ("exponencial", exponencial)
print ("multiplicação" , multiplicação)
print ("media= ", media)
ContaSuprema = (exponencial*resto)//quociente
print ("Conta Suprema", ContaSuprema)


a= 1
b= 2

#exemplo 1
print ( " o numero que está em a é %d, e em b é de %d " %(a,b))
print (" %d indica um numero inteiro")
        
#exemplo 2
print ( " o numero que está em a é %.2f e em b é de %.2f " %(a,b))
print (" indica um numero float")

#exemplo 3
print ( " o numero que está em a é",a, " e em b é de ",b)
print (" indica um numero ")


#exemplo 4
print ( " o numero que está em a é {} e em b é de {} " .format(a,b))
print (" indica um numero")

#exemplo 5
print (f' o numero que está em a é {a} e em b é {b}')
print ("indica um numero ")
