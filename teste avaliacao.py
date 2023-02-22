modelos= []
consumo= []
def entrada_carro():
    for i in range (4):
        a=input()
        modelos.append(a)
    return a


def entrada_consumo():
    for w in range (4):
        b= int(input())
        consumo.append(b)
    return b


def economico():
    C=min(consumo)
    V= consumo.index(C)
    H= modelos[V]
    return H


def main():
    entrada_carro()
    entrada_consumo()
    print(economico())

main()
