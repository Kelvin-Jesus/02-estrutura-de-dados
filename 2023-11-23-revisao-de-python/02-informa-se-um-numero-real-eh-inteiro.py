# Projete uma função que informe se um determinado número real 
# também é um inteiro. A seguir, faça uma função principal (main)
# que peça para o usuário digitar um número e informe se ele é um
# real ou um real inteiro.

def eh_inteiro(n: float) -> bool:
    '''
    Verifica se um número real *n* também é um número inteiro.
    Se for inteiro, retorna True. Se for apenas real, retorna False.
    Exemplos
    >>> eh_inteiro(10.0)
    True
    >>> eh_inteiro(1.2)
    False
    '''
    """Outra soluçao seria if n - int(n) == 0"""
    return n.is_integer()


def main():
    '''
    Função principal: 
    Pede para o usuário digitar um número e informa se ele é real ou se ele é real e inteiro.
    '''
    n = float(input("Digite um número inteiro ou real: "))
    print()
    
    ehInteiro = eh_inteiro(n)
    if ( ehInteiro ):
        return print("É Inteiro!")
        
    return print("É Real!")


if __name__ == "__main__":
    main()