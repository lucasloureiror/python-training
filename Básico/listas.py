"""
Listas - Todos os temas teóricos nesse comentário

Fatiamento: lista[inicio: fim: passo]

Append: lista.append('A') - funcão que insere um elemento na última posição da lista

Insert: lista.insert(0, 'A') - Função que insere numa posição um elemento.

Pop:  lista.pop() - remove o último elemento da lista

Del: del(lista[3:5]) - remove os elementos do indice 3 até o 4 e os outros elementos movem.

Clear: lista.clear() - remove todos os itens

Extend: lista.extend(lista2) - Coloca os itens da lista2 na lista.

Range: lista = list(range(1,10)) - Cria uma lista com os elementos de 1 a 9.

Join: Junta objetos iteráveis com um parâmetro de como juntar.

Split: Divide strings em uma lista de strings separadas por espaço. string.split(' ')

Enumerate: Enumera elementos de objetos iteráveis por meio do desempacotamento de uma lista.

Desempacotamento de lista: Técnica utilizada para pegar alguns elementos de uma lista e colocar o restante em outra lista
"""



#         0     1   2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#        -5   -4   -3   -2    -1

#FATIAMENTO - imprime do 0 até o 2;

print(lista[0:3])


#Desempacotamento

n1,n2,n3, *resto_da_lista = lista;
#n1 é o A, n2 é o B e o resto tá no resto da lista

*resto_da_lista, n1, n2,n3 = lista
#Os últimos 3 elementos estão em n1, n2 e n3 e os primeiros na outra lista.

#Sintaxe recomendada é criar uma outra lista com nome de "_" no lugar de resto_da_lista se vc não for usar esse resto.




#Imprime o indice e o valor de um objeto iterável
for indice, valor in enumerate(lista):
    print(indice, valor)


lista_na_lista = [

    [0,2],
    [1,4],
    [10,10],
]