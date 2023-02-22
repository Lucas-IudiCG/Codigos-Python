# Exercicio 1

print(" dado dois números, eu calcularei, sua soma, sua subtração, sua multiplicação, sua divisão, sua divisão trancada, seu modulo,e um elevado ao outro")
N1=int(input("o Primeiro número sendo: "))
N2=int(input("o Segundo número sendo: "))

Soma = N1 + N2
Sub = N1- N2
Multi= N1*N2
Div = N1/N2
DivT = N1//N2
Mod = N1%N2
Exp = N1**N2

print("Respectivamente: ",Soma,Sub, Multi,Div,DivT,Mod,Exp)


# Exercicio 2

print(" Temperatura em graus celsius,transformarei em Fahrenheit: ")

C= int(input( "Temperatura em graus celsius: "))
L=C*1.8
F= L+32

print(" è igual a",F,"graus Fahrenheit")


# Exercicio 3

print(" olá caro apreciador de refrigerantes")
C1 = int(input(" quantas latas de 350 ml você comprou:"))
C2 = int(input(" quantas garrafinhas de 600 ml você comprou:"))
C3 = int(input(" quantas garrafas de 2 litros você comprou:"))

R1 = C1*350
R2 = C2*600
R3 = C3*2000

R4 = (R1+R2+R3)/ 1000

print(" logo você comprou",R4,"litros de Coca-Cola")


# Exercicio 4
print("o incrivel programa de calculo de tamanho de escada")
a= float(input("Qual o angulo da escada? "))
Escada= float(input("Qual o distancia da escada ,em metros, até a parede ? "))

import math

a1 = math.cos(math.radians(a))
print(a1)
E2= int(Escada/a1)
print("A escada deverá ter ",E2,"metros")

# Exercicio 5

Conta= float(input("Vai rachar em 3, quanto que deu a conta do bar: "))
And1 = float(Conta/3)
And2 = int(Conta/3)
Car1 = float(Conta/3)
Fel= float(Conta/3)

A2 = And1- And2
C2 = Car1 - And2
Fel1= Fel + A2 + C2

print("Então respectivamente,André,Carlos e Felipe precisaram pagar")
print(And2,And2,Fel1)

# Exercicio 6

dia1 = int( input("Amigo gostaria de saber sua idade em segundos?, eu preciso do dia de nascimento: "))
mes1 = int(input("E qual mes, digite o numero do mes,: "))
ano1 = int(input(" Qual o ano da data de nascimento? "))
ano2 = int(input("Qual o ano atual:" ))

ano3 = ano2-ano1
ano4 =ano3*12
mesA = ano4+mes
diaX = mesA+dia
diaZ = diaX*30
seg = diaZ*86400

print("apos uma conta, nem um pouco precisa, voce tem aproximadamente, ",seg)
