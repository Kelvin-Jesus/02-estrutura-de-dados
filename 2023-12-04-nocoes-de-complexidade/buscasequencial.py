
"""
Arquivo: buscaSequencial.py 
Adaptado do código de Ken A. Lambert
"""
def buscaseq(item: int, l: list) -> tuple:
    '''
    Retorna a posição do *item* na *lyst*, se encontrado
    ou -1 caso contrário
    Retorna tb o número iterações realizadas
    '''
    pos = 0
    iter = 0
    while pos < len(l):
        iter += 1
        if item == l[pos]:
            return pos, iter
        pos += 1
    return -1, iter


def mediaDeIteracoes(l: list) -> float:
    totalIter = 0
    for i in l:
        pos, iter = buscaseq(i, l)
        totalIter += iter
    return totalIter/len(l)


def main() -> None:
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Iterações da busca sequencial para uma lista de", len(l),"elementos.")
    pos, iter = buscaseq(1, l)
    print("\nMelhor caso ( Pos =", pos, "):\nIterações =", iter)
    pos, iter = buscaseq(15, l)
    print("\nPior caso ( Pos =", pos, "):\nIterações =", iter)
    iter = mediaDeIteracoes(l)
    print("\nCaso médio:\nIterações =", iter)

if __name__ == "__main__":
    main()