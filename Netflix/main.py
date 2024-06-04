
#LIMPANDO O TERMINAL DO VS CODE
import os
import time
os.system ("cls || clear")


class Usuario(): #não precisava do ()

    def __init__(self, nomeUsu, emailUsu, planoUsu):

        #LEMBRE-SE, NÃO FICAR PRESO AO MESMO NOME 
        self.nome = nomeUsu
        self.email = emailUsu
        self.lista_plano = ['basic', 'premium', 'platina'] #LISTA DE PLANOS DISPONIVEIS

        #GARANTINDO MAIS UMA VEZ SE O PLANO ESTA DISPONIVEL
        if planoUsu in self.lista_plano:
            self.plano = planoUsu
        else:
            raise Exception ("Plano Invalido")
        
        #RECEBENDO UM NOVO PLANO + GARANTINDO QUE ELE É VALIDO
    def mudarPlano (self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print("plano invalido")

    def ver_filmes (self):
        if cliente.plano == "basic":

            print ("01 - LAGOA DOS PATOS")
        
        elif cliente.plano == "premium":
            print("02 - RAMBO")

        elif cliente.plano == "platina":
            print("O filme disponivel sua categoria - 03 - BAD BOYS 4")

        
        confirmação = input ("\nComeçar a assistir? ")



#COLOCANDO VALORES + ARMAZENANDO A CLASS EM UMA NOVA VARIAVEL 
cliente = Usuario (
    nomeUsu = input ("Digte o seu nome: "),
    emailUsu = input ("Digite o seu email: "),
    planoUsu = input ("Digite qual o seu plano (basic, premium, platina): "),
)

os.system("cls || clear")

#PLANO ANTERIOMENTE
print(f"O plano do cliente atual é: {cliente.plano}")

#ENVIANDO UM NOVO PLANO
opcaoPlano = input ("\nDeseja mudar de plano: ")

if opcaoPlano.lower()  == "s":
    novoPlano = input ("Qual o plano que vc deseja? (basic, premium, platina)? ")
    cliente.mudarPlano(novoPlano)

elif opcaoPlano.lower() != "s":
    print(f"\nO seu plano ainda continuar como: {cliente.plano}")    


time.sleep(5)
os.system("cls || clear")

cliente.ver_filmes()
