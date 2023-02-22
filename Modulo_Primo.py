def EhPrimo(N):
    X=N
    V=0
    while X>=1:
        Z= (N/X)- (N//X)
        X=X-1
        if Z== "0":
            V=V+1

    if V >2:
        print("Não é primo")
    else:
        print("é primo")
