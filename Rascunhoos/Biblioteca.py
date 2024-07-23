import os
os.system("cls || clear")
import time


#Criar um sistema de Biblioteca com 4 funcionalidades

'''
resultado  = (numLidas / numTotal ) * 100

print (f"Então vc leu cerca de {resultado:.2f}% do seu livro")

'''

#LISTA DE USUARIOS
listaUsu = []

#DECORAÇÃO
def tabelaPrincipal():
    print("CÓDIGO  -  DESCRIÇÃO")
    print("#1 \t-  Cadastro de Usuário")
    print("#2 \t-  Compra de Livro")
    print("#3 \t-  Empréstimo ou Devolução")
    print("#4 \t-  Cadastro de Livro")
    print("-"*35)

    try: #TENTE ISSO
        opcao = int(input("Digite a sua opção: "))
        return opcao

    except ValueError: # SE (EXCEPT = EXCETO) DÊ ESSE ERRO (ValueError)
        print("Erro: A opção deve ser um valor numérico inteiro.")
        return None  # Retorna None ou outro valor para indicar um erro
    
def tabelaCompras ():
    print ("CÓDIGO   - \tLIVRO \t\t - \t\tPREÇO")
    print (" #1\t - Caminhos do Destino   - \tR$15 ")
    print (" #2\t - Além das Estrelas     - \tR$20 ")
    print (" #3\t - Entre o Sol e a Lua   - \tR$25 ")
    print (" #4\t - A Sombra do Passado   - \tR$30 ")
    print (" #5\t - O Poder da Imaginação - \tR$35 ")

def cadastrarUsuario (listaUsu):
    nome = input ("Digite o seu nome completo: ")
    login = input ("Digite o seu login: ")
    senha = input ("Digite a sua senha: ")
    
    usuario = {
        "nome": nome,
        "login" : login,
        "senha": senha
        
    }

    listaUsu.append(usuario)
    return listaUsu

opcaoUsu = tabelaPrincipal()


print(opcaoUsu)


match opcaoUsu:
    case 1:
        os.system("cls")
        cadastrarUsuario(listaUsu)
        print(listaUsu)


# ====================================================================
'''
# EXERCICIO 3 - PORCENTAGEM DE LEITURA
import os

import time


numTotal = int (input ("Quantas paginas tem esse livro? "))

numLidas = int (input ("Quantas paginas você já leu? "))

resultado  = (numLidas / numTotal ) * 100

print (f"Então vc leu cerca de {resultado:.2f}% do seu livro")'''