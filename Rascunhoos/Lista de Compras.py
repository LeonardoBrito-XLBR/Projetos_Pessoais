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

lista = ['melancia', 'abacaxi', 'uva']
print (f"Aqui é sua lista de compras atual {lista}")

confirmação = input ("Deseja acresentar mais um produto (s/n) ? ")

if confirmação == "s":
    produto = input ("Digite o seu produto aqui: ")
    
lista.insert(0,f"{produto}") #INSERINDO um intem na posição x,

os.system ("cls || clear")

print (f"Sua nova lista atualizada: {lista}")