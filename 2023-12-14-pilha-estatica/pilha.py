from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
from multiprocessing import Value
from vetor import Vetor

@dataclass
class Item:
    valor: str

class Pilha:

    def __init__(self, tamanhoMaximo: int) -> None:
        self.TAMANHO_MAXIMO = tamanhoMaximo
        self.elementos = Vetor(tamanhoMaximo)
        self.topo = -1 # Durante as aulas foi utilizado 0.

    def estaVazia(self) -> bool:
        """
        >>> p0 = Pilha(0)
        >>> p1 = Pilha(5)
        >>> p0.estaVazia()
        True
        >>> p1.estaVazia()
        True
        """

        return self.topo == -1
    
    def estaCheia(self) -> bool:
        """
        >>> p0 = Pilha(2)
        >>> p1 = Pilha(1)
        >>> p1.empilha(Item('a'))
        >>> p0.estaCheia()
        False
        >>> p1.estaCheia()
        True
        """

        return self.topo == self.TAMANHO_MAXIMO - 1
    
    def elementoTopo(self) -> Item:
        """
        >>> p0 = Pilha(4)
        >>> p0.empilha(Item('Z'))
        >>> p0.empilha(Item('Y'))
        >>> p0.elementoTopo().valor
        'Y'
        """
        if self.estaVazia():
            raise ValueError('Pilha está vazia')
        
        return deepcopy(self.elementos[self.topo])
            
    
    def empilha(self, elemento: Item) -> None:
        """
        >>> p0 = Pilha(1)
        >>> p0.empilha(Item('a'))
        >>> p0.elementoTopo().valor
        'a'
        """
        if self.estaCheia():
            raise ValueError('Pilha Cheia')
        
        self.topo += 1
        self.elementos[self.topo] = deepcopy(elemento)

    def desempilha(self) -> None:
        """
        >>> p0 = Pilha(1)
        >>> p0.empilha(Item('a'))
        >>> p0.desempilha()
        >>> p0.estaVazia()
        True
        """
        if self.estaVazia():
            raise ValueError('Pilha está vazia')
        
        self.topo -= 1

    def exibe(self):
        if self.estaVazia():
            raise ValueError('A Pilha está vazia')

        print('Pilha: \n')
        for i in range(self.topo, -1, -1):
            print("┌───┐")
            print(f"│ {self.elementos[i].valor} │")
            print("└───┘")

    def esvazia(self) -> None:
        self.topo = -1