"""

Condicionais: IF, ELIF, ELSE.

Identação: Python não tem chave, então tem que se atentar com a identação.

"""

idade_min = 18

print("Bem vindo a porta da boate, entrada permitida apenas para maiores de 18")

idade = input("Qual é a sua idade?\n")

if int(idade) > idade_min:

    print("Você tem idade para entrar na boate")

elif int(idade) == idade_min:
    print("Você tem idade para entrar na boate")

else:
    print("Você não tem idade para entrar na boate")