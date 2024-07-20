import random

num = random.randint(0, 10)

print(f"O número sorteado foi: {num}")

player = {
"nome": "Chaves",
"ataque": 2,
"vida": 10,
}

monstro = {
"nome": "Ghatry",
"ataque": 5,
"vida": 10,
}


while True:
    num = random.randint(0, 10)
    print(f"O número sorteado foi: {num}")

    if num % 2 == 0:
        player['vida'] -= 1
        print(f"A vida do jogador agora é: {player['vida']}")
    else:
        print("O numero é ímpar")

    continuar = input("\nDeseja continuara batalha? ")
    print ()
    if continuar == 'nao':
        break

#CONTINUAR DEPOIS DAQUI E ANTES DAQUI

#EXIBIR DETALHAMDAMENTE AS SITUACOES ABAIXO
# FAZER UM COMBATE
# TERMINAR O MONSTRO
# 23/07/2024

print (f"O nome: {player['nome'],  player['vida'], player ['ataque']}")