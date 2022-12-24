nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if nome and idade: #String vazia é avaliada como valor falso!
        print(f"Seu nome é {nome}")
        print(f"Seu nome invertido é {nome[::-1]}")
        if " " in nome:
            print("Seu nome contém espaço!")
        else:
            print("Seu nome não contem espaço!")
        
        print(f"Seu nome contém {len(nome)} letras")

        print(f"A primeira letra do seu nome é {nome[0]}")

        print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios")
