"""
Conjuntos, também chamados de set, são estruturas de dados mutáveis semelhantes a da matemática.

- Sem index
- Não garantem ordem dos elementos na forma que você coloca.
- Iteráveis
- Não possui elementos repetidos, sendo eficientes para remover valores duplicados.
- Não aceita tipos mutáveis (lista, dicionário e etc)
"""

#Criando um set
s1 = set('Lucas') #O set itera sobre os elementos e coloca eles de uma forma específica.
s1 = {"Lucas"} #Agora o set vai receber o valor Lucas como string e não irá iterar.
print(s1)

#Adicionando um elemento no set com add
s1.add("Adicionei")

#Adicionando qualquer coisa no set, inclusive mutáveis, com o método update
s1.update([1,2,3]) #Ele converte a lista para o set

print(s1)

#Removendo um elemento do set
s1.remove("Adicionei")

print(s1)

#Apagando todos os elementos do set
s1.clear()

print(s1)


#Operadores Matemáticos de conjuntos:
    #1. União: Une os dois sets
    #2. Interseção: Mostra os elementos que pertecem a ambos os sets
    #4. Diferença: Mostra os itens presentes apenas no set da esquerda
    #5. Diferença Simética: Mostra os itens que não estão em ambos
            #Consultar a documentação se precisar usar alguma dessas operações.
