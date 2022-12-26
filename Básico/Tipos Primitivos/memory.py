"""

Atribuição de tipos de dados imutáveis (=): Copia o valor

Mutável: Aponta para o mesmo valor na memória

"""

texto = "Texto apontando para esse espaço na memória"

#GC pegou o texto anterior
texto = "Novo texto para a variável apontar"

listaA = ["Lucas", "Lucão"]

listaB = listaA #Apontando para o endereço na memória da lista A.

print(listaB)

listaA[0] = "Lucão"

print(listaB)

listaA = ["Nova lista", "Testando"]

print(listaB) #Continuo imprimindo Lucão e Lucão
