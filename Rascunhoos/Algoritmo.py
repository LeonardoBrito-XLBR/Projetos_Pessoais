import os 

os.system ("cls || clear")

medidas = []
resposta: bool

for i in range (3):
    lado = int (input (f"Digite o tamanho do seu { i + 1} lado: "))
    medidas.append(lado)

if medidas == medidas:
    print ("Essas medidas e de um triangulo escaleno")
else:
    print ("Essas medidas nao e de um triangulo escaleno")
