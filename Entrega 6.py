
Teste =str("")
print("Operações possiveis")
print("Soma = +")
print("Subtração = -")
print ( "Multiplicação = *")
print (" Divisão = /")
print ("Sair = 0")


while Teste != "0":
    Teste = input("Comando: ")
    if Teste =="0":
        Teste ="0"
        print(" Programa Finalizado")

  
    elif Teste == "+" or Teste == "-" or Teste == "*" or Teste == "/"  or Teste == "0" or Teste == "H":
        print(" Digite dois números:")
        N1= float(input())
        N2= float(input())
        
        if Teste =="+":
            X= N1 + N2
            print(" O Resultado é:",X)
        elif Teste == "-":
            X =N1 -N2
            print ("O Resultado é:",X)
        elif Teste =="*":
            X= N1* N2
            print (" O Resultado é:",X)
        elif Teste =="/":
            if N2 == 0:
                print(" NÃO DIVIDE POR ZERO")
            else:
                X= N1/N2
                print (" O Resultado é:",X)
                S = N2
              
        elif Teste =="0":
            Teste ="0"
            print(" Programa Finalizado")
    else:
        print(" Comando Invalido")
