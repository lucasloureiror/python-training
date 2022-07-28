"""

:s - Texto (string)
:d - Inteiros (int)
:f - Float
:.(numero)f - Quantidade de casas decimais
:(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO DE DADO -s,d,f)


"""

#Redução de casas decimais

num1 = 10
num2 = 3

divisao = num1/num2

print("{:.2f}".format(divisao))
print(f"{divisao:.2f}")





#Aumentando casas decimais de um número


num3= 1;

print(f"{num3:0<10.1f}")

#Coloca mais 10 zeros à direita.


#Formatando Strings

nome = "Lucas Loureiro"
print(nome.lower())
print(nome.upper())
print(nome.title())