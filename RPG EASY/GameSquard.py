import os
os.system("cls || clear")
from random import randint


lista_npcs = []

player = {
    "nome": "GunShort",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
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


def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)
    
def exibir_npc(npc):
    print(
        f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}"
    )

def exibir_player():
    print(
        f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
    )

def resert_player ():
    player['hp'] = player ['hp_max']

def resert_npc (npc):
    npc['hp'] = npc ['hp_max']

def level_up ():
    if player ['exp'] >= player ['exp_max']:
        player ['level'] += 1
        player ['exp'] = 0
        player ['exp_max'] = player ['exp_max'] * 2
        player["hp_max"] += 20

#MOMENTO DAS BATALHAS 
def iniciar_batalha(npc):
    
    while player ["hp"] > 0 and npc['hp'] > 0:
        atacar_player (npc)
        atacar_npc(npc)
        exibir_info_batalha(npc)
    
    if player ['hp'] > 0:
        print (f"O {player['nome']} GANHOU E ADQUIRIU {npc['exp']} DE EXP! ")
        player['exp'] += npc ['exp']
        exibir_player()
    
    else:
        print (f"O {npc['nome']} DERROTOU O {player['nome']}!")
        exibir_npc(npc)
    
    level_up()
    resert_player()
    resert_npc(npc)

# ATACANDO O NPC
def atacar_npc(npc):
    npc['hp'] -= player['dano']


# ATACANDO O PLAYER
def atacar_player(npc):
    player['hp'] -= npc['dano']


gerar_npcs(5)
#exibir_npcs()


def exibir_info_batalha (npc):
    print (f"Player: {player['hp']} || {player['hp_max']}")
    print (f"NPC: {npc['nome']}: {npc ['hp']} || {npc['hp_max']}")
    print('======================================\n')

npc_selecionado = lista_npcs[0]

#outra maneira de formatar um print

iniciar_batalha (npc_selecionado)
iniciar_batalha (npc_selecionado)
iniciar_batalha (npc_selecionado)
iniciar_batalha (npc_selecionado)
iniciar_batalha (npc_selecionado)
exibir_player ()

print (f"Vida do NPC: {npc_selecionado['hp']}")
