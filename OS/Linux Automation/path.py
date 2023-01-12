"""
1.Módulo os.path

2.Conceito: Módulo que oferece funções para trabalhar
com caminhos de arquivos em todos os OS, sem se preocupar
com diferentes raízes do sistema. 

3.join: Função que junta strings em um único caminho específico do OS em questão

4.split: divide o caminho em uma tupla de pasta e arquivo.

exists: verifica se um caminho especificado existe

ESSE MÓDULO NÃO FAZ I/O, APENAS LIDA COM CAMINHOS DE ARQUIVOS

"""

import os

caminho = os.path.join('primeiro', 'segundo', 'terceiro', 'arquivo.txt') 
print(caminho)
#Imprime: primeiro\segundo\terceiro

print(os.path.split(caminho))
#Imprime: ('primeiro\\segundo\\terceiro', 'arquivo.txt')

print(os.path.exists(caminho))
#Imprime falso pq o caminho não existe