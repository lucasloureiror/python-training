#Estrutura que enumera iteráveis

lista = ["Lucas", "Lucas2"]

listaEnumerada = enumerate(lista)

for item in lista:
    print(next(listaEnumerada))

#Enumerate são consumíveis, uma vez que depois de consumidos ficam com o ponteiro no último elemento

for indice, nome in enumerate(lista):
    print(indice, nome) #Aqui imprime o índice e o objeto