#Prova N1

# Exercicio 1

valor1 = input("digite um numero")

valor2 = input("digite um outro numero")

resultado = float((int(valor1) + int(valor2)))/2

print(resultado)


# Exercicio 2

a= input()

b= input()

print(a+b)


# Exercicio 4

n1 = int(input('Número 1:'))

n2 = int(input('Número 2:'))

if (n1%n2==0 and n1>n2):

    print ('N1 é divisivel por n2 e maior que n2')

elif (n2%n1==0 and n2>n1):

    print ('N2 é divisivel por n1 e maior que n1')

else:

    print('os números não atendem os requisitos acima')


# Exercicio 5 (O Programa não roda, Por erro de sintaxe no elif)

print('Digite 2 números')

n1 = int(input())

n2 = int (input())

if n1+n2>0:

  print('soma positivo')

elif:

  print('soma negativo')

else:

  print('soma zero')



# Exercicio 8

a = int(input("Digite o valor inteiro de a: "))

b = int(input("Digite o valor inteiro de b: "))

 

x = a // b

y = a % x

z = y ** 2


print('z =', z)

# Exercicio 9

salario=float(input('Salário:'))

if salario <1000:

    salario += 100

elif salario <2000:

    salario+=200

elif salario<3000:

    salario+=300

elif salario<4000:

    salario+=400

else:

    salario+=500

print('Salário final = R$ %.2f ' %salario)



#Exercicio 10

print(float(3) + 3)
