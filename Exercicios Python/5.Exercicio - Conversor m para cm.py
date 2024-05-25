import os
os.system ("Cls||clear")

metros = float (input ("Qual o metro: "))

centimetros  = metros * 100

centimetros = "{:.0f}".format(centimetros)

print (f"o seu metro em centimetro: {centimetros}cm")
