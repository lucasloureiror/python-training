""""

For in

Função Range: Enumera elementos no loop.

1. Argumentos em ordem: start, stop, step.

range (5,10,1)
Start = Começa no 5
Stop = para no 10
Step = pula de 1 em 1

Continue: vai pra proxima iteração do loop;
Break: Sai do loop;
Pass: Continua no código

"""

#Iterando uma string com python

texto = 'Olá, o meu nome é Lucas!'

for letra in texto:
    print(letra)


tamanho_texto = len(texto)

for indice in range (tamanho_texto):
    print(texto[indice])


for letra in texto:
    print(letra);
    if letra.lower().startswith('l'):
        print("Existe letra com L")
else:
    print("Acabei de passar pela string")