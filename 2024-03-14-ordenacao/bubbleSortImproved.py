def bubbleSortImproved(lista: list) -> list:
    tamanhoDaLista = len(lista)
    i = 0
    trocou = True
    while trocou:
        trocou = False
        for j in range(tamanhoDaLista-i-1):
            # compara
            if lista[j] > lista[j+1]:
                # troca
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True

        i += 1

    return lista

print(bubbleSortImproved([0, 26, 3, 4, 56, 6]))