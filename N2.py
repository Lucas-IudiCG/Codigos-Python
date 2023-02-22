# Carros 2

modelos= []
consumo= []
def entrada_carro():
    a=input()
    print(a)
    return a


def entrada_consumo():
    b= int(input())
    return b


def economico():
    for i in range (4):
        x=entrada_carro()
        modelos.append(x)
    for w in range (4):
        y=entrada_consumo()
        consumo.append(y)

    
    C=min(consumo)
    V= consumo.index(C)
    H= modelos[V]
    print(H)

    
            
    




economico()
        
    
