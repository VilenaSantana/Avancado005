nomes = ["Ana", "Bruno", "Carlos"]

try:
    indice = int(input("Digite um número de 0 a 2: "))
    print("Nome:", nomes[indice])
except IndexError:
    print("Erro: esse índice não existe na lista.")
except ValueError:
    print("Erro: digite um número válido.")
