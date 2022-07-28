#Verificar se o nome do usuário tem 5 e 6 letras.

nome = input("Qual é o seu nome?\n")

if len(nome) < 5:
    print("Seu nome é curto")

elif len(nome) > 6:
    print("Seu nome é muito grande")

else:
    print("Seu nome é normal")