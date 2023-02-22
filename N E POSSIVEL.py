def exibeMsg():
    print("F- Conversão de Fahrenheit para Celsius")
    print ("C- Conversão de Celsius para Fahrenheit")

def getConvertTo():
    opcao = input(" Digite F ou C: ").upper()
    while opcao!="C" and opcao!= "F":
        opcao = input(" Digite F ou C: ").upper()
    return opcao

def exibeFahrenheitTOCelsius(start, end):
    for f in range (start, end+1):
        c = 5/9*(f-32)
        print ("%d °F = %.1f °C " %(f,c))

def exibeCelsiusTOFahrenheit(start, end):
    for c in range (start, end+1):
        f = (c*9/5)+32
        print (" %d °C = %.1f °F " %(c,f))

        
def main():
    exibeMsg()
    op = getConvertTo()
    start= int(input("Início do intervalo: "))
    end = int(input("Fim do intervalo: "))
    if op == "C":
        exibeCelsiusTOFahrenheit(start, end)
    else:
        exibeFahrenheitTOCelsius(start, end)


main()
