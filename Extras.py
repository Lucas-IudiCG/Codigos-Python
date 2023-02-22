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
        x1= time.split(":")[0]
        x2= time.split(":")[1]
        x3= time.split(":")[2]
        Quantidade.append(x1)
        Preco.append(x2)
        Produto.append(x3)
        


V= str(input("Pressione um botão para o programa Calcular: "))
Read.close()

A=len(Quantidade)
A=A-1


while A >-1:
    B1=int(Quantidade[A])
    B2=int(Preco[A])
    Total_1= B1*B2
    Lista.append(Total_1)
    A=A-1

Produto.reverse()
A2=len(Quantidade)
A2= A2-1

while A2>-1:
    print("Produto:",Produto[A2]," - Subtotal: R$ ",Lista[A2])
    A2= A2-1


print("Total do pedido: R$ ",sum(Lista))

V= str(input("Pressione um botão para acabar o Programa"))
