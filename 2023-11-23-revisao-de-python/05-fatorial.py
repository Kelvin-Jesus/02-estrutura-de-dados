# Projete uma função que calcule o fatorial de um número. 
# A seguir, faça uma função principal que peça para o usuário 
# digitar um número inteiro n e informe o valor de n!.

def fatorial(n: int) -> int:
    '''
    Calcula o fatorial do número inteiro *n*.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(2)
    2
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    >>> fatorial(5)
    120
    '''
    if n == 0:
        return 1

    return fatorial(n - 1) * n


def main():
    '''
    Pede para o usuário digitar um número inteiro e informa o fatorial.
    '''
    fat = int(input("Digite o valor a calcular o fatorial: "))

    print(f"O fatorial é {fatorial(fat)}")
    

if __name__ == "__main__":
    main()