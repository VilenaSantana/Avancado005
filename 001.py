try:
    print(x)

except NameError:
    print("Variavel invalida")
try:
 x = 10 + "5"
except TypeError:
    print("Erro de tipo")