#String é qualquer coisa dentro de aspas, simples, duplas ou triplas.
#string = str.

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



