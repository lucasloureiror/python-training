numero = input("Digite um número inteiro: ")

def checkNumber(number):
    if numero % 2 == 0:
        print("O número é par!")
    else:
        print("O número não é par!")

try:
    numero = int(numero)
    checkNumber(numero)
except:
    print("Não digitou um número inteiro")






