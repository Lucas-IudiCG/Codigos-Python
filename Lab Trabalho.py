# Exercicio 5
print("Calcule a distancia entre um observador e um prédio, sabendo a altura do prédio e o angulo entre a visão do observador e o topo deste mesmo prédio, desconsiderando as dimensões do observador nulas")
predio = float(input( "Tamanho do prédio (em metros): "))
angulo= float(input("Qual o angulo entre a visão do observador e a rua? "))

import math

angulo1 = math.tan(math.radians(angulo))

Resposta5= predio/angulo1

print (" Logo, o observador está á ",math.ceil(Resposta5), " metros de distância do prédio")


# Exercicio 3

print("Calcule o volume do cilindro,tendo seu raio e sua altura")
altura= float (input("Altura do cilindro: "))
raio = float(input("Raio da base: "))

import math

pi = math.pi

area= (raio**2)*pi
Resposta3 = altura*area

print ("O volume desta cilindro é, aproximadamente %.2f"%Resposta3)


#Exercício 1

print("Calcule as projeções, a altura, e a hipotenusa de um triangulo retângulo, sabendo os catetos do mesmo: ")

cateto1 = float(input("Valor do primeiro cateto: "))
cateto2 = float(input("Valor do segundo cateto: "))

hipotenusa2 = cateto1**2 + cateto2**2

import math

hipotenusa1 = math.sqrt(hipotenusa2)

projeçãoDoCateto1 = cateto1**2/hipotenusa1

projeçãoDoCateto2 = cateto2**2/hipotenusa1

Altura2 = projeçãoDoCateto1* projeçãoDoCateto2

Altura1 = math.sqrt(Altura2)

print ("Sua hipotenusa é: ",hipotenusa1)
print("Suas projeções são",projeçãoDoCateto1,projeçãoDoCateto2)
print("E sua altura é: %.2f"%Altura1)


