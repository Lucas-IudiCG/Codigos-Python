print(" Exercicio 4: Volume da lata de óleo")
n1 = float(input("que tem raio: "))
n2 = float(input("e sua altura: "))
pi = 3.1415

a= n1**2
v= a*n2*pi
print("  Se considerar PI= 3.1415, Então seu volume será aproximadamente:", v)


      
print("Exercicio 5: Dado 3 numeros quaisquer")
A= float(input("o primeiro numero sendo: "))
B= float(input("o segundo numero sendo: "))
C= float(input("e o terceiro sendo: "))

X = A**2
Y = B**2
Z = C**2

Soma = X+Y+Z
Soma2 = A+B+C
L = Soma2**2

print(" Então a soma de seus quadrados será: ", Soma )
print ("Então o quadrado de sua soma será: ", L)



print(" Exercicio 6: programa do espetaculo teatral")

C = float(input("Você gastou quanto para realizar o espetaculo: "))
I = float(input("E por quanto, você vendeu cada ingresso:"))

N6 = C/I

print("logo você vai precisar vender %d ingressos, para equivaler ao custo do espetaculo" %(N6))

L23 = C*0.23 +C
LC = L23/I

print("E para você ter lucro de 23 por cento, você precisa vender %d ingressos: "%(LC))
