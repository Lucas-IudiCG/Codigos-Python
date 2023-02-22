a=5
b=5
def Somarec (a,b):
    if b==0:
        return a
    else:
        return Somarec(a,b-1)+1

print(Somarec(a,b))
