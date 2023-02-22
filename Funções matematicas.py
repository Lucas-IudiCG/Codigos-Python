#Funções matematicas

a=float (input(" Valor de a: "))
b=float (input(" Valor de b: "))
x=float (input(" Valor de x: "))

N1 =3*b
N2 =5*x
N3= a**2
N4= N2**3
N5 = N1**0.5

y= (N3+N5)/N4


print(" Y é igual á: ",y)


import math
r = int(input('Raio: '))
v = 4/3 * math.pi * math.pow(r,3)
print(f'Volume {v}')
