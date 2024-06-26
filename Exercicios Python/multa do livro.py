import os

os.system("cls || clear")


'''
FAZER O SISTEMA DE MULTA BASEADO NO DIA QUE A PESSOA DIGITAR 


TAREFAS ====

terminar a def
parar o laco
conferir o print
'''

dataVencimento = {

    'data': 26,
    'mes': 6,
    'ano': 2024,
}

def verifacao (dataUsu, mes, ano, dataVencimento):
    resultado = dataUsu - dataVencimento

    if dataUsu in dataVencimento:
        print (f"A sua data de vencimento expirou a: {resultado} ")




while True:
    dataUsu = int(input("Digite aqui a sua data de vencimento: "))
    mes = int(input('Digite o Mês: '))
    ano = int(input('Digite o Ano: '))
    parar = input ("Quer PARAR? (S/N): ")
    if parar != 'S':
        break 

print(f"A data de vencimento: {dataUsu}/{mes}/{ano} registrada!")
verifacao (dataUsu, mes, ano, dataVencimento)

