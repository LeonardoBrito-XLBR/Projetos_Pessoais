def verificar_item_no_vetor(vetor, item):
    return item in vetor

# Exemplo de uso da função
vetor = [1, 2, 3, 4, 5]


item = int (input(" escolha 1 - 5:   ")) 

if verificar_item_no_vetor(vetor, item):
    print(f"O item {item} está presente no vetor.")
else:
    print(f"O item {item} não está presente no vetor.")
