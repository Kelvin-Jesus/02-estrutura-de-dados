def divisores(n: int) -> list:
    '''
        Retorna, para um dado um número inteiro *n*, uma lista contendo os seus divisores.
        Exemplos
        >>> divisores(5)
        [1, 5]
        >>> divisores(10)
        [1, 2, 5, 10]
        >>> divisores(15)
        [1, 3, 5, 15]
        >>> divisores(150)
        [1, 2, 3, 5, 6, 10, 15, 25, 30, 50, 75, 150]
    '''
    listaDeDivisores: list = []
    for i in range(1, n+1):
        if (n % i) == 0:
            listaDeDivisores.append(i)

    return listaDeDivisores

def main():
    n: int = int(input("Digite um número inteiro: "))

    print(f"Os divisores de {n} são: {divisores(n)}")

if __name__ == "__main__":
    main()