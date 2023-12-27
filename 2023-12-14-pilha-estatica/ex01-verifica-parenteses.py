"""
Compiladores em geral precisam determinar se os símbolos de parênteses que aparecem nas expressões estão balanceados corretamente.
- I.e., para cada ( deve haver um ) correspondente.

Escreva uma função verificaParenteses() que, dada uma string contendo uma expressão, verifique se ela está com os parênteses balanceados Utilize uma pilha para registrar a ocorrência dos parênteses.

Exemplos:
-> (2 * (a + b)) = Parênteses BALANCEADOS
-> empilha(Item(c)) = Parênteses DESBALANCEADOS
-> print(round(media_aritmetica(n1, n2, n3),1)) = Parênteses BALANCEADOS
-> (2 * (a + b) = Parênteses BALANCEADOS
-> empilha(Item(c))) = Parênteses DESBALANCEADOS

"""
from __future__ import annotations
from pilha import Pilha, Item

def parentesesEstaoBalanceados(expressao: str) -> bool:
    """
    >>> parentesesEstaoBalanceados('(2 * (a + b))')
    True
    >>> parentesesEstaoBalanceados('empilha(Item(c))')
    True
    >>> parentesesEstaoBalanceados('print(round(media_aritmetica(n1, n2, n3),1))')
    True
    >>> parentesesEstaoBalanceados('(2 * (a + b)')
    False
    >>> parentesesEstaoBalanceados('empilha(Item(c)))')
    False
    """
    pilha = Pilha(10)

    for caractere in expressao:
        if caractere == '(':
            pilha.empilha(Item(caractere))

        elif caractere == ')':
            if pilha.estaVazia():
                return False
            
            pilha.desempilha()

    return pilha.estaVazia()

def main():
    expressao = input('Digite uma expressão com parênteses: ')
    if parentesesEstaoBalanceados(expressao):
        print('Parênteses BALANCEADOS')
    else:
        print('Parênteses DESBALANCEADOS')

if __name__ == "__main__":
    main()

