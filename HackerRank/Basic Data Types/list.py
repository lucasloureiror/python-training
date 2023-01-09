def funcao(N):
    lista = []
    for i in range(N):
        entrada = input()
        entrada = entrada.split()
        
        if entrada[0] == "insert":
            lista.insert(int(entrada[1]), int(entrada[2]))
        elif entrada[0] == "print":
            print(lista)
        elif entrada[0] == "remove":
            lista.remove(int(entrada[1]))
        elif entrada[0] == "append":
            lista.append(int(entrada[1]))
        elif entrada[0] == "sort":
            lista.sort()
        elif entrada[0] == "pop":
            lista.pop()
        elif entrada[0] == "reverse":
            lista.sort(reverse=True)

if __name__ == '__main__':
    N = int(input())
    funcao(N)
    
