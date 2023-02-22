#Exemplo

def rfunc1(n):
    print(n)
    if n > 0:
        rfunc1(n-1)


def rfunc2(n):
    if n == 1:
        return 1
    else:
        return n + rfunc2(n-1)


N=int(input("Digite um numero natural: "))
print(rfunc2(N))

