# Exercicio 5

nota =0
lst=[]
AcimaDe7 =[]
AbaixoDe7=[]
def MSG():
    print: ("Quantos alunos tem na classe?")

def Entrada():
    for i in range (4):
        n= float(input())
        while n<0 and n> 10:
            n = float(input(" Nota inválida: "))
        lst.append(n)
        
        
def X_media ():
    media = sum(lst)/4
    return media


def main():
    MSG()
    for i in range(10):
        Entrada()
        X_media()
        if nota >= 7:
            AcimaDe7.append(nota)
            print(AcimaDe7)
        else:
            AbaixoDe7.append(nota)
            print(AbaixoDe7)
        
    print(AcimaDe7)
    print(AbaixoDe7)

main()

