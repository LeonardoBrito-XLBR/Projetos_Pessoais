import os
os. system("cls || clear")

import time

tempo= [1,2,3,4,5]
idade = int (input ("Quantos anos você tem? "))
trabalhoTime =  int (input ("Você tem quantos trabalhando? "))

caculo =  2024 - trabalhoTime
Time =  2024 - caculo


if idade > 65 or Time >= 30:
    situação = "Você esta preste a receber a sua aposentadoria"
else:
    situação = "Trabalhe mais alguns anos amigo"

os.system ("cls || clear")

print ("Aguarde... Calculando a sua Aposentadoria")

for i in reversed (tempo):
    print (f"Analisando {i}...")
    time.sleep (2)

os.system ("Cls || clear")
pronto = input ("Preparado? ")

if pronto != 'sim':
    print ("não entendi amigo? Oxem")

else:
    print (f"{situação}")

