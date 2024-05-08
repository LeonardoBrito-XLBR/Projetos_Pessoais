class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro

# Inicialização dos vetores
avioes = [None] * 4
assentos_disponiveis = [0] * 4
reservas = []

def registrar_avioes():
    print("Informe o número de cada avião:")
    for i in range(4):
        avioes[i] = input(f"Avião {i+1}: ")

def registrar_assentos_disponiveis():
    print("Informe a quantidade de assentos disponíveis para cada avião:")
    for i in range(4):
        assentos_disponiveis[i] = int(input(f"Assentos disponíveis para o avião {avioes[i]}: "))

def realizar_reserva():
    if len(reservas) >= 10:
        print("Limite de reservas atingido!")
        return
    
    numero_aviao = input("Informe o número do avião: ")
    if numero_aviao not in avioes:
        print("Este avião não existe!")
        return
    
    indice_aviao = avioes.index(numero_aviao)
    if assentos_disponiveis[indice_aviao] == 0:
        print("Não há assentos disponíveis para este avião!")
        return
    
    nome_passageiro = input("Informe o nome do passageiro: ")
    reservas.append(Reserva(numero_aviao, nome_passageiro))
    assentos_disponiveis[indice_aviao] -= 1
    print("Reserva realizada com sucesso!")

def consultarA():
    numero_aviao = input("Digite o número do avião para consulta: ")
    if numero_aviao not in avioes:
        print("Este avião não existe.")
    else:
        reservas_aviao = [r for r in reservas if r.numero_aviao == numero_aviao]
        if not reservas_aviao:
            print("Não há reservas realizadas para este avião.")
        else:
            print("Reservas para o avião", numero_aviao)
            for res in reservas_aviao:
                print(f"Passageiro: {res.nome_passageiro}")
    
def consultarP():
   nome_passageiro = input("Digite o nome do passageiro para consulta: ")
   reservas_passageiro = [r for r in reservas if r.nome_passageiro == nome_passageiro]
   if not reservas_passageiro:
       print("Não há reservas realizadas para este passageiro.")
   else:
       print("Reservas para o passageiros", nome_passageiro)
       for res in reservas_passageiro:
           print(f"Avião: {res.numero_aviao}")
           
def menu():
    print("\nMenu:")
    print("1. Registrar número de cada avião")
    print("2. Registrar quantitativo de assentos disponíveis em cada avião")
    print("3. Reservar passagem aérea")
    print("4. Realizar consulta por avião")
    print("5. Realizar consulta por passageiro")
    print("6. Encerrar")

# Programa principal
while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        registrar_avioes()
    elif opcao == 2:
        registrar_assentos_disponiveis()
    elif opcao == 3:
        realizar_reserva()
    elif opcao == 4:
        consultarA()
    elif opcao == 5:
        consultarP()
    elif opcao == 6:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")



