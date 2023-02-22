# Bazinga!

T=int(input())
for i in range (T):
    Sheldon,Raj = str(input()).split(" ")            
    if Sheldon=="papel" and Raj=="pedra" or Sheldon=="tesoura" and Raj=="papel" or Sheldon=="pedra" and Raj =="lagarto" or Sheldon=="lagarto" and Raj=="Spock"or Sheldon =="Spock" and Raj=="tesoura" or Sheldon=="tesoura" and Raj =="lagarto" or Sheldon=="lagarto" and Raj=="papel" or Sheldon=="papel" and  Raj =="Spock" or Sheldon=="Spock" and Raj =="pedra" or Sheldon=="pedra" and Raj=="tesoura":
        print("Caso #1: Bazinga!")
    elif Sheldon =="lagarto" and Raj=="tesoura" or Sheldon=="papel" and Raj=="tesoura" or Sheldon=="pedra" and Raj=="papel" or Sheldon=="lagarto" and Raj =="pedra" or Sheldon=="Spock" and Raj=="lagarto" or Sheldon =="tesoura" and Raj=="Spock" or Raj =="lagarto" and Sheldon=="papel" and Raj=="tesoura" or Sheldon=="Spock" and Raj=="papel" or Sheldon=="pedra" and Raj== "Spock" or Sheldon =="tesoura" and Raj=="pedra":
        print ("Caso #2: Raj trapaceou!")
    else:
        print ("Caso #3: De novo!")

    
