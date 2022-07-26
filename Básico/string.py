#String é qualquer coisa dentro de aspas, simples, duplas ou triplas.
#string = str.

from ast import While


print('String com aspas simples')

print("String com aspas duplas")




#Manipulando as aspas no print

print("Essa é uma 'string' (str)")

#Usei aspas duplas pra abrir a string e coloquei uma aspa simples na string.


#Uso de string raw no print

print("Aqui coloco \n uma quebra de linha")
print(r"Aqui eu evito a quebra de linha \n com o raw")


#Caractere de escape na string

print("Com a \"barra invertida\" eu consigo fugir do parâmetro")





"""
Fstring é uma forma de formatar uma string em um print.

Format também permite formatar uma string

"""

nome = "Lucas"
idade = 27

print(nome, 'tem', idade, 'anos de idade')

#Agora vem formatado com fstring.
print(f'{nome} tem {idade} anos de idade')

#Agora com format
print('{} tem {} anos de idade'.format(nome, idade))




"""

Função len, que determina o número de caracteres em tipos de dados.

"""

usuario = "Lucas"

quantidade_de_caracteres = len(usuario)

print(quantidade_de_caracteres)
print(usuario.__len__())


#Possível converter tipos numéricos para String e assim conseguir determinar a quantidade
numero = 123456

print(len(str(numero)))


"""

Índice de Strings: Ideia que toda string é um vetor.
Fatiamento: Pegar partes de uma string da seguinte forma nome[2:5]
Funções built-in

"""

indice = "Lucas Loureiro Rodrigues"

#Imprimir o caracter na terceira posição da string
print(indice[3])

#Índice -1 pega o último caracter.


""""

ITERAÇÃO DE STRING COM WHILE

"""
frase = 'o rato roeu a roupa do rei de roma'

tamanho_frase = len(frase)

contador = 0

while contador < tamanho_frase:
    print(frase[contador])
    contador += 1

