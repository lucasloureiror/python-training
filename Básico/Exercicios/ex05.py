
def inserir(lista):
    entrada = input("Digite o item a ser inserido: ")
    lista.append(entrada)
    return lista


def apagar(lista):
    entrada = input("Digite o item que você deseja apagar: ")

    if entrada in lista:
        lista.remove(entrada)
        print(f"Apaguei o seu objeto: {entrada}")
        return lista
    else:
        print("Objeto não encontrado!")

def listar(lista):
    
    print(lista)


lista = []



while True:
    entrada = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar\n")

    if entrada == "i":
        inserir(lista)

    elif entrada == "a":
        apagar(lista)
    
    elif entrada == "l":
        listar(lista)
    
    else:
        break;