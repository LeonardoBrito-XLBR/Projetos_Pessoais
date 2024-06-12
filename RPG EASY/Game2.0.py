'''
implementar

'''


import os
import time
os.system("Cls || clear")
from random import randint 


def contagem ():
    tempo = [5,4,3,2,1]

    for i in tempo:
        time.sleep(1)
        print(f"{i}...")


numero = randint(0,10)

nome = input ("Digite o seu nome: ")

os.system("Cls || clear")
          
print (f"Caro jogador {nome} você esta preste a morrer\nVamos testar sua sorte!")
confirmação = input ("Preparado? ")

os.system("Cls || clear")
contagem()

if numero % 2 == 0:
    print (f"\nO dado girou e caiu no {numero}!\nIsso significa Vida 💖")
elif numero % 2 != 0:
    print (f"\nO dado girou e caiu no {numero}!\nIsso significa Morte 💀")

time.sleep(2)
print ("\n\nFIM DO JOGO!")
'''
valeu 
'''