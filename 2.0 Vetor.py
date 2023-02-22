def GeraVetor():
    Size= int(input("Digite o tamanho do vetor: "))
    vet=[0]*Size
    H=Size-1
    X=0
    while H > -1:
        vet[X]=int(input("Digite um Número: "))
        H=H-1
        X=X+1
    H2=len(vet)
    H2=H2-1
    H3=H2
    Y=0
    final = True
    while H2 > -1 and Y<H3 and final == True:
        if vet[Y] <vet[Y+1]:
            H2=H2-1
            Y=Y+1

        else:
            final = False

    if final == False:
        print("Não é crescente")

    else:
        print("É crescente")
        




GeraVetor()

