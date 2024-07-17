import os 

os.system ("cls || clear")

medidas = set()

stop = False

while stop == False:
    for i in range (3):
        lados = (input (f"Digite o {i+1} lado do seu triangulo: "))

        if lados in medidas:
            print ("Valor duplicado não é permitido")
            stop = True
        else:
            medidas.add(lados)

print (f"{medidas}")