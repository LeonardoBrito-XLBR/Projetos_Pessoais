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
    valorFinal = valor + custo
    return valorFinal


    return 

taxa = 0.10

custo = 50

#formas de printa
print (somaImposto (taxa, custo))


