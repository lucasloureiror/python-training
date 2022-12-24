numero = input("Digite um número menor que 10\n")

while int(numero) >= 10:
    print("Você digitou um numero invalido")
    numero = input("Digite um número menor que 10\n")

#O else faz parte do laço e portando comandos de break também impedem ele de rodar.
else:
    print("O número tem o valor correto")