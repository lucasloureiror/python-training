""""
Introdução ao assunto:

Try = Vai tentar executar o código
except = ocorreu algum erro ao tentar executar
"""

entrada = input("Digite um número: ")

try:
    print(int(entrada))
except: 
    print("Ocorreu um erro ao tentar fazer a ação acima pois um número não foi digitado!")

