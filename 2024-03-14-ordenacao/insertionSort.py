def insertionSort(lista: list, tamanhoDaLista: int) -> list:
    for i in range(1, tamanhoDaLista):
        chave = lista[i]
        j = i

        while j > 0 and lista[j-1] > chave:
            lista[j] = lista[j-1]
            j -= 1

        lista[j] = chave

    return lista

print(insertionSort([4, 7, 2, 5, 4, 0], 6))