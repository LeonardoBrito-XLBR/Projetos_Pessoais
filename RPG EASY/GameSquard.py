import os
os.system("cls || clear")
from random import randint


'''

COLOCAR AS VARIAVEIS EM CAMCASE 
LEMBRE-SE - 02/06/2024 > 22:12

'''


lista_npcs = []

player = {
    "nome": "GunShort",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,

}


def criar_npc(level):
    #level = randint(0, 50)
    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp_max": 100 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }
    
    return novo_npc


def gerar_npcs(num_npcs):

    for x in range(num_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)


def exibir_npcs ():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']} || Level: {npc['level']} || Dano: {npc['dano']} || Vida: {npc['hp']} || Exp: {npc['exp']}" )


''''
CONSERTA 

'''


def iniciar_batalha(npc):
    atacar_player (npc)
    atacar_npc(npc)
    exibir_info_batalha(npc)


def atacar_npc(npc):
    npc['hp'] -= player['dano']


def atacar_player(npc):
    player['hp'] -= npc['dano']


gerar_npcs(5)
#exibir_npcs()


def exibir_info_batalha (npc):
    print (f"Player: {player['hp']} || {player['hp_max']}")
    print (f"NPC: {npc['nome']}: {npc ['hp']} || {npc['hp_max']}")

npc_selecionado = lista_npcs[0]

#outra maneira de formatar um print

iniciar_batalha (npc_selecionado)


