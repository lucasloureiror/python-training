hora = input("Que horas são agora?\n")

def verificaHora(hora):
    if hora < 12:
        print("Bom dia!")
    elif hora < 18:
        print("Boa tarde!")
    elif hora < 24:
        print("Boa noite!")
    else:
        print("Hora inválida!")

try:
    hora = int(hora)
    verificaHora(hora)
except:
    print("Não digitou um número inteiro!")