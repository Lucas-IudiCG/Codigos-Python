# Desafio!

Bissexto= int(input("digite um número e direi se ele vai ser ou for bissexto: "))
Teste1 = Bissexto/4
Teste2 =Bissexto//4
Teste3 = Bissexto/100
Teste4 = Bissexto/400
Teste5 =Bissexto//400

if Bissexto < 1000 or Bissexto > 9999:
    print(" Ano inválido")

    
elif Teste1 == Teste2 or Teste4 == Teste5 and Teste3 != 0:
    print("Esse ano é bissexto")


else:
    print("Esse ano não é bissexto")
