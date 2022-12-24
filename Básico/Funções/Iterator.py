"""

Iterável = O dado que vai oferecer algo para ser iterado

Iterador = Objeto que sabe entregar um valor por vez

next = entregar o próximo valor

iter = entregue o iterador

"""


texto = "Algo para ser iterado"

iterador = iter(texto);


#Isso que um for faz em um objeto iterável
while True:
    try:
        print(next(iterador))
    except StopIteration: #Pegando o erro de StopIteration
        break;

#O for fazendo a mesma coisa
for letra in texto:
    print(letra)

