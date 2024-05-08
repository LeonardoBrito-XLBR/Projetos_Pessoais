#LIMPANDO O TERMINAL DO VS CODE
import os
os.system ("cls || clear")


class Usuario(): #não precisava do ()

    def __init__(self, nome, email, plano):

        #LEMBRE-SE, NÃO FICAR PRESO AO MESMO NOME 
        self.nome = nome
        self.email = email
        self.lista_plano = ['basic', 'premium'] #LISTA DE PLANOS DISPONIVEIS

        #GARANTINDO MAIS UMA VEZ SE O PLANO ESTA DISPONIVEL
        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception ("Plano Invalido")
        
        #RECEBENDO UM NOVO PLANO + GARANTINDO QUE ELE É VALIDO
    def mudarPlano (self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print("plano invalido")

    # def ver_filmes (self, filme):

#COLOCANDO VALORES + ARMAZENANDO A CLASS EM UMA NOVA VARIAVEL 
cliente = Usuario ("Leonardo", "leopato@gmail.com", "basic")

#PLANO ANTERIOMENTE
print(f"O plano do cliente era: {cliente.plano}")

#ENVIANDO UM NOVO PLANO
cliente.mudarPlano("balalal")

#ALTUALIZANDO O PLANO
print(f"O novo plano do cliente {cliente.plano}")