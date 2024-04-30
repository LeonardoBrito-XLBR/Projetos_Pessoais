#Redesenhar o Codigo com o Preço na Tabuada - 26 /04 / 2024 > 15:50

import os
os.system ("cls || clear")

# DECLARANDO AS VARIÁVEIS PARA NÃO DAR ERRO
subTotal = 0
conjunto = []

def tabuada():
    print ("="*36)
    print("CÓDIGO  -     DESCRIÇÃO  -   PREÇO")
    print ("-"*36)
    print(" 1      -      Pizza     -   R$ 20")
    print(" 2      -      Burguer   -   R$ 15")
    print(" 3      -      Sorvete   -   R$ 10")
    print(" 4      -      Frango    -   R$ 25")
    print(" 5      -      Churrasco -   R$ 30")
    print(" 6      -      Salada    -   R$ 10")
    print(" 7      -      Lasanha   -   R$ 12")
    print(" 0      -      PARAR     -  XXXXXXX")
    print("="*36)
  
def pagamento():
    print("="*35)
    print('CÓDIGO - DESCRIÇÃO - CONDIÇÃO')
    print("-"*35)
    print('  1    -  À vista  -  desconto 10%')
    print('  2    -  Cartão   -  acrescimo 10%')
    print("="*35)

print ("Olá tudo bem - Seja Bem - Vindo(a) ")
iniciar = input('Deseja começar o atendimento (s ou n)? ').lower()

while iniciar == "s":
    os.system("cls || clear")
    tabuada() #MENU
    opcao = int(input("\nO que você vai querer? "))
            
    match opcao:
        case 1:
            prato = "1 - Pizza de Calabresa"
            conjunto.append (prato)
            preco = 20
            print(f"{prato} = R${preco}")
                    
        case 2:
            prato = "2 - Burguer"
            conjunto.append (prato)
            preco = 15
            print(f"{prato} = R${preco}")
                    
        case 3:
            prato = "3 - Sorvete "
            conjunto.append (prato)
            preco = 10
            print(f"{prato} = R${preco}")
                    
        case 4:
            prato = "4 - Frango "
            conjunto.append (prato)
            preco = 25
            print(f"{prato} = R${preco}")
        case 5:
            prato = "5 - Churrasco "
            conjunto.append (prato)
            preco = 30
            print(f"{prato} = R${preco}")
                    
        case 6:
            prato = "6 - Salada"
            conjunto.append (prato)
            preco = 10
            print(f"{prato} = R${preco}")
                    
        case 7:
            prato = "7 - Lasanha"
            conjunto.append (prato)
            preco = 12
            print(f"{prato} = R${preco}")
        
        case 0:
            break
                    
    subTotal += preco 
                    
          
    iniciar = input('\nGostaria de adicionar mais um prato (s / n): ')
    
os.system("cls || clear")

pagamento() #TABELA DOS PREÇO
formaPag = int(input("Qual a forma de pagamento: "))
    
match formaPag:
    case 1:
        somaPreçoCond = subTotal - (subTotal / 10)
        
    case 2:
        somaPreçoCond = subTotal + (subTotal /10)
        
    case _:
        print("Ops... erro")

somaPreço = subTotal / 10

os.system("cls || clear")
print(f"O total de refeições escolhidas {len(conjunto)}")
print (f"O seu pedido escolhido: {conjunto}")
print(f"O valor do Adicional ou Desconto: {somaPreço}")
print(f"O SubTotal: {subTotal}")
print(f"O Valor Total a pagar: {somaPreçoCond}")
saida = input ("Pronto? ")
os.system("cls || clear")
print ("BOAS COMPRAS E VOLTE SEMPRE")


