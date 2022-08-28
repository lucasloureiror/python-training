"""

Atividade do módulo Básico do Curso de Python

A ideia era fazer um contador em um único laço de python, mas um contador deve ser de acréscimo e o outro de decréscimo

"""

decrescente = 10;
crescente = 0;

while(crescente <= 8):
    print(crescente, decrescente)
    crescente += 1
    decrescente -= 1



#Solução do professor utilizou a função enumerate 
#for p,r in enumerate(range(10,1,-1)):
#    print(p,r)
