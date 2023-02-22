# 1 Exercicio

N5dig = int(input(" Numero de 5 digitos: "))

A1 = N5dig//10000
R1 = N5dig%10000
A2 = R1//1000
R2 = R1%1000
A3 = R2//100
R3 = R2%100
A4 = R3//10
R4 = R3%10

print (A1)
print (A2)
print (A3)
print (A4)
print (R4)


# 2 Exercicio

Compra = int(input(" Valor da Compra: "))


N100 = Compra//100
V1 = Compra%100
N50 = V1//50
V2 =  V1%50
N20 = V2//20
V3 =  V2%20
N10 = V3//10
V4 = V3%10
N5 = V4//5
V5 = V4%5
N2 = V5//2
V6 = V5%2
N1 = V6

print ("Notas de 100 R$",N100)
print ("Notas de 50 R$",N50)
print ("Notas de 20 R$",N20)
print ("Notas de 10 R$",N10)
print ("Notas de 5 R$",N5)
print ("Notas de 2 R$",N2)
print ("Notas de 1 R$",N1)
