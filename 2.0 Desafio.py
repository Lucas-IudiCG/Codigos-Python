X=int(input("Digite um número inteiro: "))
K=0
for i in range(X):
    K+=1
    if K<=X:
        for j in range(K):
            print("*", end=" ")
        print("\n")
