# Projete uma função que retorne, para um dado número inteiro
# n, uma lista contento todos os pares de números inteiros cujo o
# produto resulta em n.

# Por simplicidade, considere que o par (x, y) é diferente de (y, x)
def conjuntos(n) -> list[set[int]]:
    '''
        Dado número inteiro *n*, a função retorna uma lista contento todos 
        os conjuntos(conjuntos) de números inteiros cujo o produto resulta em *n*.
        Exemplos
        >>> pares(5)
        [{1, 5}]
        >>> pares(10)
        [{1, 10}, {2, 5}]
        >>> pares(15)
        [{1, 15}, {3, 5}]
        >>> pares(150)
        [{1, 150}, {2, 75}, {50, 3}, {5, 30}, {25, 6}, {10, 15}]
    '''
    lista: list[set[int]] = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            produtoEhIgualAhN = (i * j) == n

            if produtoEhIgualAhN:
                conjunto = set()
                conjunto.add(i)
                conjunto.add(j)

                if conjunto not in lista:
                    lista.append(conjunto)

    return lista

def main():
    n: int = int(input("Digite um número inteiro: "))

    print(f"Os conjuntos de inteiros que resultam em {n} são: {conjuntos(n)}")

if __name__ == "__main__":
    main()