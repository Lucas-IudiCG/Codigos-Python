# Calculadora Infernal

S = 0
Teste =str("")
print("Operações possiveis")
print("Soma = +")
print("Subtração = -")
print ( "Multiplicação = *")
print (" Divisão = /")
print ("Salvar um Valor = S")
print ("Resgatar um valor Salvo = R")
print ("Sair = 0")
print ("Rever Operações = H")
    
while Teste != "0":
    Teste = input()
    if Teste =="0":
        Teste ="0"
        print(" Programa Finalizado")
        
   elif Teste == "R":
       print(S)
       print(" Digite R1 ou R2, para colocar o valor salvo no N1 ou N2, Respectivamente")
       R = input()
       if R=="R1":
           N1= S
           Teste =input()
           elif Teste == "+" or Teste == "-" or Teste == "*" or Teste == "/" or Teste == "S" or Teste == "0" or Teste == "H":
               print(" Digite dois números:")
               N2= (input())
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
           elif Teste == "S":
               print("Digite S1, para Salvar o Primeiro número,")
               print("Digite S2, para Salvar o Segundo número,")
               print("Digite S3, para Salvar o Resultado número,")
               A = input()
               if A=="S1":
                   S = N1
                   print("Valor Salvo")
               elif A =="S2":
                   S = N2
                   print("Valor Salvo")
               elif A =="S3":
                   S =X
                   print("Valor Salvo")
               else:
                   print (" Comando Invalido")
           elif Teste =="0":
               Teste ="0"
               print(" Programa Finalizado")
           elif Teste =="H":
               print("Operações possiveis")
               print("Soma = +")
               print("Subtração = -")
               print ( "Multiplicação = *")
               print (" Divisão = /")
               print ("Salvar um Valor = S")
               print ("Sair = 0")
               print ("Rever possiveis operações = H")
           else:
               print(" Comando Invalido")


           

       elif R=="R2":
           N2= S
           Teste =input()
           elif Teste == "+" or Teste == "-" or Teste == "*" or Teste == "/" or Teste == "S" or Teste == "0" or Teste == "H":
               print(" Digite dois números:")
               N1= (input())
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
           elif Teste == "S":
               print("Digite S1, para Salvar o Primeiro número,")
               print("Digite S2, para Salvar o Segundo número,")
               print("Digite S3, para Salvar o Resultado número,")
               A = input()
               if A=="S1":
                   S = N1
                   print("Valor Salvo")
               elif A =="S2":
                   S = N2
                   print("Valor Salvo")
               elif A =="S3":
                   S =X
                   print("Valor Salvo")
               else:
                   print (" Comando Invalido")
           elif Teste =="0":
               Teste ="0"
               print(" Programa Finalizado")
           elif Teste =="H":
               print("Operações possiveis")
               print("Soma = +")
               print("Subtração = -")
               print ( "Multiplicação = *")
               print (" Divisão = /")
               print ("Salvar um Valor = S")
               print ("Sair = 0")
               print ("Rever possiveis operações = H")
           else:
               print(" Comando Invalido")
       else:
           print (" Comando Invalido")
       
        
    elif Teste == "+" or Teste == "-" or Teste == "*" or Teste == "/" or Teste == "S" or Teste == "0" or Teste == "H":
        print(" Digite dois números:")
        N1= (input())
        N2= (input())
        
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
        elif Teste == "S":
            print("Digite S1, para Salvar o Primeiro número,")
            print("Digite S2, para Salvar o Segundo número,")
            print("Digite S3, para Salvar o Resultado número,")
            A = input()
            if A=="S1":
                S = N1
                print("Valor Salvo")
            elif A =="S2":
                S = N2
                print("Valor Salvo")
            elif A =="S3":
                S =N3
                print("Valor Salvo")
            else:
                print (" Comando Invalido")
        elif Teste =="0":
            Teste ="0"
            print(" Programa Finalizado")
        elif Teste =="H":
            print("Operações possiveis")
            print("Soma = +")
            print("Subtração = -")
            print ( "Multiplicação = *")
            print (" Divisão = /")
            print ("Salvar um Valor = S")
            print ("Sair = 0")
            print ("Rever possiveis operações = H")
    else:
        print(" Comando Invalido")
