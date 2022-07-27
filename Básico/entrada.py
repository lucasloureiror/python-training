"""

A entrada de dados é quase que integralmente mediada pela função input.

A função input SEMPRE retorna uma string.

"""

nome = input("Qual é o seu nome?\n")

print(nome)


#Fazendo casting de um valor

idade = input("Qual é a sua idade?\n")

ano_de_nascimento = 2022 - int(idade)

print(ano_de_nascimento)