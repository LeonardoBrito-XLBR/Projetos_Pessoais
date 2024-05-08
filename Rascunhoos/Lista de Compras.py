'''
Fazer uma lista de compras removiel atrvaes do
numero que a pessoa quer tirar - referenta ao item

vetor 
remove 
def > comandos

for para anexar um numero a cada item - enumerar 

'''

import os
os.system("cls  clear")

#CRIANDO UMA LISTA PARA RECEBER OS ITENS
lista = []

#Laço para pedir 3 primeiros itens
for i in range (3):
    
    produto = input ("O que vc deseja colocar na sua lista: ")
    lista.append(produto)

#Pausando
print (f"Esses são seus itens atualmente: {lista}")

#Criando um laço para repetir
while True:
    confirmação = input ("Deseja acresentar mais um produto (s/n) ? ")

    if confirmação == "s":
        produtoAdd = input ("Digite o seu produto aqui: ")
        lista.insert(0,f"{produtoAdd}") #INSERINDO um intem na posição x,
    else:
        break

#EXIBINDO AS LISTAS DE COMPRAS
os.system ("cls || clear")

print (f"Sua nova lista atualizada: {lista}")