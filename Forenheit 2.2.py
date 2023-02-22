def exibeMsg():
    print ("Conversão de Farenheit para Celsius - F")
    print ("Conversão de Celsius para Farenheit - C")

def getConvertTo():
    N = str(input("Digite F ou C:")).upper
    if N =="C":
        return C
    elif N == "F":
        return F
    else:
        return O
        

def  exibeFahrenheitTOCelsius(F):
    F = x-32
    return F*5/9
    
def exibeCelsiusTOFahrenheit (C):
    C= (y+32)
    return C*1.8

def principal ():
    exibeMsg()
    N= getConvertTo()
    if N =="F":
        print(F)
    elif N == "C":
        print (C)
    else:
        print("Comando Inválido")
    
