import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Livro: 
    nome: str = 'Geração'
    preco: float = 59.90
    dataValidade: int = 25

# Criando uma instância da classe Livro
livro1 = Livro()

dataNova: int = 30

if livro1.dataValidade < dataNova:
    livro1.preco += 2
else:
    print('De boa')

print(f"{livro1.preco:.2f} foi o que você irá pagar!")

