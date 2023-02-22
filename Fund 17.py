num=int(input())
num2=int(input())
if num>0 and num2>0:
    Soma=0
    while num>0:
        while num2>0:
            Soma=Soma+num2
            num2=num2-1
        num=num-1
    print (Soma)
