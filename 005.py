try:
    numero = 10
    print(numero.upper())
except AttributeError:
    print("Erro: esse objeto não tem esse método. Erro de atributo.")
