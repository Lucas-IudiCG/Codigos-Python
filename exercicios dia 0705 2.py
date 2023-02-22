Num =[]

def Entrada():
    print(" Digite 10 números: ")
    for i in range (10):
        Num.append(float(input()))

def Inverter():
    Num.reverse()

def Saida():
    print("Números em ordem inversa")
    for x in Num:
        print(x)

def main():
    Entrada()
    Inverter()
    Saida()

main()
