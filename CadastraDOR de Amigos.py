# Lista de Exercicios de Lista 2.0

Amigos=[]
def menu():
    print("1= Cadastrar um amigo( No Final da Lista)")
    print("2= Mostar Nomes de todos os amigos)")
    print("3=Cadastrar um amigo(Inicio da Lista)")
    print("4=Remover um Nome")
    print("5=Substituir um Nome")
    print("6=Mostrar o número total de amigos Cadastrados")
    print("7=Colocar os Nomes dos amigos em Ordem Alfabetica")
    print("8=Finalizar Programa")
    

def programa():

    V=0
    while V==0:
        I= str(input("digite um codigo: "))
        if I=="1":
            A=str(input("Nome: "))
            Amigos.append(A)
        elif I == "2":
            print(Amigos)
        elif I == "3":
            A=str(input("Nome: "))
            Amigos.insert(0,A)
        elif I =="4":
            print(Amigos)
            idex=input("Número para ser Removido: ")
            X=Amigos.index(idex)
            del Amigos [X]
        elif I=="5":
            print(Amigos)
            idex=input("Número para ser Removido: ")
            X=Amigos.index(idex)
            del Amigos [X]
            Z = input("Acrescentar nome ao espaço Removido: ")
            Amigos.insert(X,Z)
        elif I =="6":
            T=len(Amigos)
            print("Número total de Amigos: ",T )
        elif I =="7":
            alfa= Amigos.sort()
            print(Amigos)
        elif I== "8":
            V+=1
            print("Programa Finalizado")

        else:
            print("Codigo Inválido")


def main():
    
    menu()
    programa()
    print(Amigos)




main()
