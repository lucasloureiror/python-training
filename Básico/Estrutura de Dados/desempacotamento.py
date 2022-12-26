lista = ["Lucas", "Lucas2", "Lucas3"]

nome1, nome2, nome3 = lista #Desempacoto cada nome em cada variável

#Quando quero pegar apenas um valor posso jogar o resto em uma lista

nome, *resto = lista #A variável resto cria uma lista com lucas2 e lucas3

#Variável de resto com underline

nome, *_ = lista #Afirmo que o resto não será utilizado

