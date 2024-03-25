def selectionSort(lista: list, tamanhoDaLista: int) -> None:
    for indiceAtual in range(tamanhoDaLista - 1):
        indiceDoMenor: int = indiceAtual

        for proximoIndice in range(indiceDoMenor + 1, tamanhoDaLista):
            if lista[proximoIndice] < lista[indiceDoMenor]:
                indiceDoMenor = proximoIndice

        lista[indiceAtual], lista[indiceDoMenor] = lista[indiceDoMenor], lista[indiceAtual]

selectionSort([7, 5, 1, 8, 3], 5)