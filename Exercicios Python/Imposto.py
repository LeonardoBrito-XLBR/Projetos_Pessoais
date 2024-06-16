import os
os.system("cls || clear")


'''
Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa 
em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo 
para incluir o imposto sobre vendas.


FAZER A SEPARAÇÃO DOS PRODUTOS E APLICAR O ACRESSIMO NO VALOR FINAL
'''
def somaImposto (taxaImposto, custo):
    valor = taxaImposto * custo
    return valor

taxa = 10.0

custo = 50

resultado = somaImposto (taxa, custo)


print (resultado)