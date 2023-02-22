# Calculadora Infernal// fazer divisão truncada, Exponencial E Troca entre N1 e N2, Arrendodamento e modulo

S =int(0)
Teste =str("")
print("Operações possiveis")
print("Soma = +")
print("Subtração = -")
print ( "Multiplicação = *")
print ("Divisão = /")
print ("Exponencial = ^")
print ("Div. Truncada= //")
print (" Modulo = M")
print ("Anotação = A")
print ("Salvar um Valor = S")
print ("Resgatar um valor Salvo = R")
print ("Sair = 0")
print ("Rever Operações = H")
    
while Teste != "0":
    print("Digite um Comando")
    Teste = input()
    if Teste =="0":
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

    elif Teste =="A":
        Q= str(input(" Digita A1 para anotar, e A2 para ver a Anotação: "))
        if Q== "A1":
            a=str(input( "digite a1,a2,a3,a4,a5. Para escolher o slot de memoria: "))
            if a=="a1":
                NOTA1=str(input())
            elif a =="a2":
                NOTA2= str(input())
            elif a== "a3":
                NOTA3= str(input())
            elif a== "a4":
                NOTA4= str (input())
            elif a == "a5":
                NOTA5= str(input())
            else:
                print("Comando Invalido")
        elif Q == "A2":
            n= str(input("escolha a nota que deseja (n1,n2,n3,n4,n5,All): "))
            if n =="n1":
                print(NOTA1)
            elif n=="n2":
                print(NOTA2)
            elif n=="n3":
                print(NOTA3)
            elif n=="n4":
                print(NOTA4)
            elif n=="n5":
                print(NOTA5)
            elif n=="All":
                print(NOTA1)
                print(NOTA2)
                print(NOTA3)
                print(NOTA4)
                print(NOTA5)
            else:
                print ("Comando Invalido")
        
        else:
            print("Comando Invalido")

     
            

    elif Teste == "R":
        print(" Digite R1 ou R2, para colocar o valor salvo no N1 ou N2, Respectivamente")
        R = input()
        if R=="R2":
            print(S)
            N2=S
            print(" Digite um novo Comando: ")

            Teste =input()
            
            if Teste == "+" or Teste == "-" or Teste == "*" or Teste == "/" or Teste == "0":
                print(" Digite um número:")
                N1= float(input())
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
                elif Teste =="0":
                    Teste ="0"
                    print(" Programa Finalizado")
 
                else:
                    print(" Comando Invalido")
                    
        elif R=="R1":
            print(S)
            N1 = S
            print(" Digite um novo Comando: ")

            Teste =input()
            
            if Teste == "+" or Teste == "-" or Teste == "*" or Teste == "/" or Teste == "0":
                print(" Digite um número:")
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
                elif Teste =="0":
                    Teste ="0"
                    print(" Programa Finalizado")
        
                else:
                    print(" Comando Invalido")
                    
     
        else:
            print (" Comando Invalido")

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

            
    elif Teste == "+" or Teste == "-" or Teste == "*" or Teste == "/"  or Teste == "0" :
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
        elif Teste =="0":
            Teste ="0"
            print(" Programa Finalizado")
        
    else:
        print(" Comando Invalido")
