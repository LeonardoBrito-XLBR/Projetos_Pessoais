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


def criar_npc():
    level = randint(0, 50)
    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }
    
    return novo_npc


def gerar_npcs(num_npcs):

    for x in range(num_npcs):
        npc = criar_npc()
        lista_npcs.append(npc)


def exibir_npcs ():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']} || Level: {npc['level']} || Dano: {npc['dano']} || Vida: {npc['hp']}" )


''''
CONSERTA 

'''

#atacar_npc(npc) = npc:hp - player:dano
def atacar_npc(npc):


#atacar_player(npc) = player: hp - npc:dano




gerar_npcs(3)
exibir_npcs()
