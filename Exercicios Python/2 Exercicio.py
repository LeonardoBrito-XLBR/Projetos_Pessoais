#LIMPANDO O TERMINAL
import os
import time
os.system ("Cls || clear")


vetor = []
print ("O programa para quando vc escreve (STOP)\n")


while True:
    
    numero = input ("Digite o seu numero: ")

    if numero != 'STOP':
        vetor.append(numero)

    if numero == "STOP":
        break

#APAGANDO OS NUMEROS INSERIDOS
os.system ("cls || clear")
time.sleep (2)


#EXIBINDO OS NUMEROS
for i in (vetor):
    print (f"Os seus numeros foram: {i}")