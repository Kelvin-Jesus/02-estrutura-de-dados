# Projete uma função que receba três números inteiros 
# e retorne o maior e o menor deles, nesta ordem.

def maior_e_menor(n1: int, n2: int, n3: int) -> tuple:
    '''
    Retorna o *maior* e o *menor* dentre os inteiros *n1*, *n2* e *n3*.
    Exemplos
    >>> maior_e_menor(1, 2, 3)
    (3, 1)
    >>> maior_e_menor(5, 15, 10)
    (15, 5)
    '''
    maior = n1
    menor = n1

    if n2 > n1 and n2 > n3:
        maior = n2
    elif n3 > n1:
        maior = n3

    if n2 < n1 and n2 < n3:
        menor = n2
    elif n3 < n1:
        menor = n3

    return (maior, menor)


def main():
    '''
    Função principal: 
    Pede para o usuário digitar três números e informa o maior e o menor deles.
    '''

    n1 = int(input("Digite n1: "))
    n2 = int(input("Digite n2: "))
    n3 = int(input("Digite n3: "))

    tuplaDeMaiorMenor = maior_e_menor(n1, n2, n3)
    print(f"O maior é: {tuplaDeMaiorMenor[0]}")
    print(f"O menor é: {tuplaDeMaiorMenor[1]}")
    

if __name__ == "__main__":
    main()