import re

#Criando um objeto que guardará a expressão regular analisada (telefone)

telefoneRegex = re.compile(r"\d\d\d\d\d-\d\d\d\d")
telefone = input("Digite um número de telefone: ")
resultado = telefoneRegex.search(telefone)

print(resultado)