elif Teste =="^":
    print("Digite E1 para digitar o valor a ser elevado, ou E2 para elevar pelo N2")
    E= str(input())
    if E =="E1":
        K =float(input("Digite um numero"))
        X= N1**K
        print(X)

    elif E =="E2":
        X = N1**N2
        print(X)

    else:
        print("Comando Invalido")


elif Teste =="//":
    X= N1//N2
    print (X)



elif Teste =="M":
    D= N1//N2
    X = N1 - (D*N2)
    print(X)

