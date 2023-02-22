def exibeMsg():
    print ("Conversão de Farenheit para Celsius - F")
    print ("Conversão de Celsius para Farenheit - C")

def getConvertTo():
    N = input("Digite F ou C: ").upper()
    while N!="C" and N!="F":
        N = input("Digite F ou C: ").upper()
    return N

def  exibeFahrenheitTOCelsius(start,end):
    for f in range (start,end+1):
        c= 5/9(f-32)
        print ("%d °F = %.1f  °C" %(f,c))

        
def  exibeCelsiusTOFahrenheit(start,end):
    for c in range (start,end+1):
        f= 9/5(c+32)
        print ("%d °F = %.1f  °C" %(c,f))


def main():
    exibeMsg()
    V= getConvertTo()
    start= int(input("Início do Intervalo: "))
    end = int(input("Fim do Intervalo: "))
    if V=="F":
        exibeFahrenheitTOCelsius(start,end)
    else:
        exibeCelsiusTOFahrenheit(start,end)

main()
