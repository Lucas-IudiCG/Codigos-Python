resultado=[]
def calcular(n):
    a=0
    b=1
    for i in range(n):
        b=a+b
        a+=1
        resultado.insert(b)


calcular(5)
print(resultado)
