"""
                                         DICIONÁRIOS

1. Conceito: Estruturas de dados do tipo chave e valor, sendo que a chave pode funcionar como um índice.
2. Sintaxe dessa estrutura: {} ou a classe dict
3. Métodos úteis:
    a. len: Fala quantas chaves tem.
    b. keys: iterável com as chaves
    c. values: iterável com os valores
    d. items: iterável com chaves e valores.
    e. setdefault: adiciona valor se a chave não existe
    f. copy: retorna uma shallow copy do dict, sendo necessário atenção pois valores mutáveis serão copiados por referência ainda.
    g. get: obtém uma chave
    h. pop: Apaga um item com a chave especificada
    i. popitem: Apaga o último item adicionado
    k. update: Atualiza um dicionário com outro

"""

pessoa = {
    "Nome": "Lucas",
    "Função": "DevOps"
}

print(type(pessoa))
print(pessoa["Nome"]) #Imprindo o valor da chave nome

pessoa["LinguagemFavorita"] = "GoLang" #Adicionando a chave linguagem favorita e o valor da chave

print(pessoa)



