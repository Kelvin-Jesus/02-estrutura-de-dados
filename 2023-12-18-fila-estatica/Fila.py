from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass

from Vetor import Vetor

@dataclass
class Item:
    valor: str

class Fila():

    def __init__(self, tamanhoMaximo) -> None:
        self.TAMANHO_MAXIMO = tamanhoMaximo
        self.elementos = Vetor(tamanhoMaximo)
        self.inicio = 0
        self.fim = 0
        self.quantidadeElementos = 0

    def estaVazia(self) -> None:
        """
        >>> fila = Fila(2)
        >>> fila.estaVazia()
        True
        >>> fila.enfileira(Item('A'))
        >>> fila.estaVazia()
        False
        """
        return self.quantidadeElementos == 0
    
    def estaCheia(self) -> bool:
        """
        >>> fila = Fila(1)
        >>> fila.estaCheia()
        False
        >>> fila.enfileira(Item('A'))
        >>> fila.estaCheia()
        True
        """
        return self.quantidadeElementos == self.TAMANHO_MAXIMO

    def enfileira(self, elemento: Item) -> None:
        """
        >>> fila = Fila(2)
        >>> fila.enfileira(Item('a'))
        >>> fila.estaVazia()
        False
        """
        if self.estaCheia():
            raise ValueError('Fila já está cheia')

        self.elementos[self.fim] = deepcopy(elemento)
        self.fim = self._avanca(self.fim)
        self.quantidadeElementos += 1
    
    def desenfileira(self) -> Item:
        """
        >>> fila = Fila(1)
        >>> fila.enfileira(Item('A'))
        >>> fila.estaVazia()
        False
        >>> fila.desenfileira()
        >>> fila.estaVazia()
        True
        """
        if self.estaVazia():
            raise ValueError('Fila já está vazia')
        
        elemento = self.elementos[self.inicio]
        self.inicio = self._avanca(self.inicio)
        self.quantidadeElementos -= 1

        return elemento

    def primeiroElemento(self) -> Item:
        """
        >>> fila = Fila(1)
        >>> fila.enfileira(Item('A'))
        >>> fila.primeiroElemento().valor
        'A'
        """
        if self.estaVazia():
            raise ValueError('Fila já está vazia')

        return deepcopy(self.elementos[self.inicio])
    
    def exibe(self) -> None:
        print('Fila: inicio --> [', end='')
        i = self.inicio

        for k in range(self.quantidadeElementos):
            print(self.elementos[i].valor, end='')
            if k < self.quantidadeElementos - 1:
                print(', ', end='')

            i = self._avanca(i)
        print('] <-- fim')

    def esvazia(self) -> None:
        """
        >>> fila = Fila(1)
        >>> fila.enfileira(Item('A'))
        >>> fila.estaVazia()
        False
        >>> fila.esvazia()
        >>> fila.estaVazia()
        True
        """
        self.inicio = 0
        self.fim = 0
        self.quantidadeElementos = 0

    def tamanho(self) -> int:
        return self.quantidadeElementos

    def _avanca(self, indice: int) -> int:
        return (indice + 1) % self.TAMANHO_MAXIMO
    

p = Fila(5)
p.enfileira(Item('A'))
p.enfileira(Item('B'))
p.enfileira(Item('C'))
p.enfileira(Item('D'))
p.enfileira(Item('E'))
# p.enfileira(Item('F'))

p.exibe()
# Fila: inicio --> ['A', 'B', 'C', 'D', 'E'] <-- fim
p.desenfileira()
p.desenfileira()
p.exibe()
# Fila: inicio --> ['C', 'D', 'E'] <-- fim
p.enfileira(Item('F'))
p.exibe()
# Fila: inicio --> ['C', 'D', 'E', 'F'] <-- fim
p.esvazia()
p.exibe()
# Fila: inicio --> [] <-- fim