def funcao(S):
    Result=0
    while S> 0:
        num1 = S
        num2= num1**2
        Result= (num1/num2) + Result
        S=S-1
    return Result
