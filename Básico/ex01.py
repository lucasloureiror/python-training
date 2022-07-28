#Exercício para verificar se um número é inteiro e depois checar se é par ou ímpar.
numero = input("Digite um número inteiro\n")

if numero.isdigit():

    if int(numero) % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
else:
    print("O número digitado não foi um inteiro")
