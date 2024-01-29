from __future__ import annotations
from copy import deepcopy
from Cliente import Cliente

from Vetor import Vetor

class Fila():

    def __init__(self, tamanhoMaximo) -> None:
        self.TAMANHO_MAXIMO = tamanhoMaximo
        self.elementos = Vetor(tamanhoMaximo)
        self.inicio = 0
        self.fim = 0
        self.quantidadeElementos = 0

    def estaVazia(self) -> None:
        return self.quantidadeElementos == 0
    
    def estaCheia(self) -> bool:
        return self.quantidadeElementos == self.TAMANHO_MAXIMO

    def enfileira(self, elemento: Cliente) -> None:
        if self.estaCheia():
            raise ValueError('Fila já está cheia')

        self.elementos[self.fim] = deepcopy(elemento)
        self.fim = self._avanca(self.fim)
        self.quantidadeElementos += 1
    
    def desenfileira(self) -> Cliente:
        if self.estaVazia():
            raise ValueError('Fila já está vazia')
        
        elemento = self.elementos[self.inicio]
        self.inicio = self._avanca(self.inicio)
        self.quantidadeElementos -= 1

        return elemento

    def primeiroElemento(self) -> Cliente:
        if self.estaVazia():
            raise ValueError('Fila já está vazia')

        return deepcopy(self.elementos[self.inicio])
    
    def exibe(self) -> None:
        print('[', end=' ')
        i = self.inicio

        for k in range(self.quantidadeElementos):
            print(self.elementos[i].senha, end='')
            if k < self.quantidadeElementos - 1:
                print(', ', end='')

            i = self._avanca(i)
        print(' ]')

    def esvazia(self) -> None:
        self.inicio = 0
        self.fim = 0
        self.quantidadeElementos = 0

    def tamanho(self) -> int:
        return self.quantidadeElementos

    def _avanca(self, indice: int) -> int:
        return (indice + 1) % self.TAMANHO_MAXIMO
