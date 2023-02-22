# Exercicio 1

N0= float(input(" Digite um número: "))

if N0>0:
    print("o número é positivo")

elif 0> N1:
    print ("o número é negativo")

else:
    print ("o número é nulo")


# Exercicio 2

N1 = float(input(" Digite um número: "))
N2 = float(input(" Digite outro número: "))


if N1 > N2:
    print ("O " ,N1," é o maior")

elif N2 > N1:
    print ("O " ,N2," é o maior")

elif N1 == N2:
    print ("Os numeros tem o mesmo valor")

# Exercicio 3

Nome1= str(input(" Digite um nome: "))
Nome2= str(input(" Digite um nome: "))

if Nome1 < Nome2:
    print(" em ordem alfabetica fica: ", Nome1,Nome2)

else:
    print(" em ordem alfabetica fica: ", Nome2,Nome1)


# Exercicio 4

N3e5= float(input(" Digite um número: "))

Div = N3e5/15
Trunc = N3e5//15

if Div == Trunc:
    print( "o numero é divisivel por 3 e 5, ao mesmo tempo")

else:
    print(" o numero não é divisivel por 3 e 5, ao mesmo tempo")

# Exercicio 5

Sexo= str(input("digite o seu sexo(com apenas um digito): "))

if Sexo == 'm' or Sexo == 'M' or Sexo == 'F' or Sexo == 'f':
    print("Sexo válido!")

else:
    print("Sexo inválido")





# Exercicio 6

Ano = int(input("Para calcular a taxa de seu carro, primeiramente, precisamos saber o ano de fabricação: "))
Preco = float(input( "qual é o preço do carro: "))

if Ano <2010:
    taxa= 2.5/100
    Resultado = taxa*Preco
    print("o valor de sua taxa é igual a: ", Resultado)

    
else :
    taxa= 3.5/100
    Resultado = taxa*Preco
    print("o valor de sua taxa é igual a: ", Resultado)


# Desafio!

Bisexxto= int(input("digite um número e direi se ele vai ser ou for bisexto: "))
Teste1 = Bisexxto/4
Teste2 =Bisexxto//4
Teste3 = Bisexxto/100
Teste4 = Bisexxto/400
Teste5 =Bisexxto//400

if Bisexxto < 1000 and Bisexxto > 9999:
    print(" Ano inválido")

elif Teste1 == Teste2 or Teste4 == Teste5 and Teste3 != 0:
    print("Esse ano é bisexxto")

else:
    print("Esse ano não é bisexxto")

