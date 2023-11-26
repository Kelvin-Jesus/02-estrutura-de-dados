# Projete uma função que calcule a média aritmética de três números reais. 
# A seguir, faça uma função rincipal (main) que peça para o usuário digitar 
# três notas e imprima a média dessas notas.

def media_aritmetica(n1: float, n2: float, n3: float) -> float:
    '''
    Calcula a média artimética dos números *n1*, *n2* e *n3*.
    Exemplos
    >>> round(media_aritmetica(5, 5, 8), 1)
    6.0
    >>> round(media_aritmetica(3, 5, 6), 1)
    4.7
    >>> round(media_aritmetica(10, 5, 8.5), 1)
    7.8
    '''
    
    return (n1 + n2 + n3) / 3

def main():
    '''
    Função principal: 
    Pede para o usuário digitar três notas e imprime a média arredondada para 1 casa decimal.
    '''
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    print(f"A média é: {round(media_aritmetica(n1, n2, n3), 1)}")
    
if __name__ == "__main__":
    main()