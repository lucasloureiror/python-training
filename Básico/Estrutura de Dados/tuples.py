"""

Tupla: É uma lista imutável

"""

#Declaração de uma tupla, igual a lista, mas sem o colchete ou com parênteses

nomes = "Lucas", "Lucas2"

tupla = ("Lucas", "Lucas2")

#Tentativa de mudar um valor de uma tupla

#nomes[0] = "Teste" 
# #Não vai rodar alegando que tuple não suporta reassignment.

#Transformando uma lista em uma tupla

lista = ["Teste"]

tupla2 = tuple(lista)

print (tupla2)

