import os
from dataclasses import dataclass

os.system("cls || clear")

#lista para armazenar cada livro
biblioteca = []

#criando uma class
@dataclass
class Livro: 
    titulo: str
    autor: str
    ano: int
    categoria: str
    preco: float



#quantidade de livros
QUANTIDADE_LIVRO = 2

#solicitando cada item do livro
for i in range (QUANTIDADE_LIVRO):
    livro = Livro (

        titulo= input("Qual o nome do livro: "),
        autor=input("Qual o nome do autor: "),
        ano=int(input("Em qual ano foi lançado: ")),
        categoria=input("Qual categoria vai receber: "),
        preco = float (input("Quanto ele vai valer: ")),
        
    )

    #guardando numa lista
    biblioteca.append(livro)


print("Os Livros foram cadastrados com sucesso! ")


'''
terminar se possivel - caso não - deboa

'''