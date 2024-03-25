def bubbleSort(lista: list) -> list:
    tamanhoDaLista = len(lista)

    for i in range(tamanhoDaLista - 1):
        for j in range(tamanhoDaLista - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista
        

print(bubbleSort([0, 26, 3, 4, 56, 6]))