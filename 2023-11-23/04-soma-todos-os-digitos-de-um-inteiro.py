# Projete uma função que calcule a soma dos dígitos de um número inteiro. 
# A seguir, faça uma função principal que peça para o usuário digitar 
# um número inteiro e informe a soma dos seus dígitos.

def soma_digitos (n : int) -> int:
    '''
    Calcula a soma dos dígitos do número inteiro *n*.
    Exemplos
    >>> soma_digitos(5)
    5
    >>> soma_digitos(10)
    1
    >>> soma_digitos(123)
    6
    >>> soma_digitos(12345)
    15
    '''
    numeroComoString = str(n)
    soma = 0
    
    for i in range(0, len(numeroComoString)):
        soma += int(numeroComoString[i])

    return soma


def main():
    '''
    Pede para o usuário digitar um número inteiro e informa a soma dos seus dígitos.
    '''
    

if __name__ == "__main__":
    main()