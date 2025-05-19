lista = [10, 20, 30]

try:
    print(lista[5])
except IndexError:
    print("Erro: índice fora da lista.")
