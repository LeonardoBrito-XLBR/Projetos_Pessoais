'''


PEDIR VALIDAÇÃO DE SENHA

CRIAR UM SISTEMA DE PAGAMENTO NA TROCA DOS PLANOS 

'''


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
        
        #LISTA DE TODOS OS FILMES + PLANOS
        filmesBasic = ["RAMBO", "JACK", "PICA-PAU"]
        filmesPremium = ["GRANDE LUTADOR","ERA DO GELO 6", "KING KONG"]
        filmesPlatina = ["GIGANTE DE AÇO", "MATHEUS O GRANDE", "HOMEM ARANHA"]
    
        quantidade: int = 0

        #LISTA DE FILMES BASIC
        if cliente.plano == "basic":
            print(f"Olha {self.nome}, de acordo com seu plano, esses são os filmes disponiveis.")
            
            for i in filmesBasic:
                quantidade+=1
                print(f"{quantidade} - {i}")

            confirmaçãoBasic = int (input ("\nComeçar a assistir? "))


            if confirmaçãoBasic == 1:
                print(f"Assistindo: {filmesBasic[0]}")

            elif confirmaçãoBasic == 2:
                print(f"Assistindo: {filmesBasic[1]}")

            elif confirmaçãoBasic == 3:
                print(f"Assistindo: {filmesBasic [2]}")
            else:
                print ("Opção Inválida!")


        #LISTA DE FILMES PREMIUM
        elif cliente.plano == "premium":
            print(f"Olha {self.nome}, de acordo com seu plano, esses são os filmes disponiveis.")
            
            for i in filmesPremium:
                quantidade+=1
                print(f"{quantidade} - {i}")

                confirmação = int (input ("\nComeçar a assistir? "))


            if confirmação == 1:
                print(f"Assistindo: {filmesPremium[0]}")

            elif confirmação == 2:
                print(f"Assistindo: {filmesPremium[1]}")

            elif confirmação == 3:
                print(f"Assistindo: {filmesPremium [2]}") 
                
            else:
                print ("Opção Inválida!")

        elif cliente.plano == "platina":
            print(f"Olha {self.nome}, de acordo com seu plano, esses são os filmes disponiveis.")

            for i in filmesPremium:
                quantidade+=1
                print(f"{quantidade} - {i}")
            
            if confirmação == 1:
                print (f"Assistindo :{filmesPlatina[0]}")
            
            elif confirmação == 2:
                print (f"Assistindo :{filmesPlatina[1]}")
            
            elif confirmação == 3:
                print (f"Assistindo :{filmesPlatina[2]}")
            
            else: 
                print ("Opção Inválida!")
            

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
print("\nPipoca? Refrigerante? Doces?")


