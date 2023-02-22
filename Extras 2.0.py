finalRead = False
string_vazia =""
Lista =[]
Produto=[]
Quantidade=[]
Preco= []


Read = open("Itens_pedidos.txt", "r")


print("Preço de mercado:")

while not finalRead:
    linha= Read.readline()
    if linha == string_vazia:
        finalRead= True
    else:
        
        time =linha.rstrip()
        x1= time.split(":")
        Lista.append(x1)
        print(Lista)
        



Read.close()

A=len(Lista)
A=A-1
