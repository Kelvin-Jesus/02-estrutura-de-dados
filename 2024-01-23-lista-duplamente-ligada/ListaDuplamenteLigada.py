from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Item:
    valor: int

@dataclass
class No:
    elemento: Item | None
    anterior: No | None = None
    proximo: No | None = None

class ListaDuplamenteLigada:

    def __init__(self):
        self.inicio = No(None)
        self.inicio.anterior = self.inicio
        self.inicio.proximo = self.inicio

    def estaVazia(self) -> bool:
        return self.inicio.proximo == self.inicio

    def _insere(self, elemento: Item, noAntecessor: No) -> None:
        novoNo = No(elemento)
        novoNo.anterior = noAntecessor
        novoNo.proximo = noAntecessor.proximo
        noAntecessor.proximo.anterior = novoNo
        noAntecessor.proximo = novoNo

    def insereNoInicio(self, elemento: Item) -> None:
        self._insere(elemento, self.inicio)

    def insereNoFim(self, elemento: Item) -> None:
        self._insere(elemento, self.inicio.anterior)

    def insereNaPosicao(self, elemento: Item, posicao: int) -> None:
        noAntecessor = self.inicio

        if posicao >= 0:
            for i in range(posicao):
                noAntecessor = noAntecessor.proximo
        elif posicao < 0:
            for i in range(0, posicao, -1):
                noAntecessor = noAntecessor.anterior

        self._insere(elemento, noAntecessor)

    def _remove(self, noAntecessor: No) -> None:
        noAntecessor.proximo.proximo.anterior = noAntecessor
        noAntecessor.proximo = noAntecessor.proximo.proximo

    def removeNoInicio(self) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')

        self._remove(self.inicio)
    
    def removeNoFim(self) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')      

        self._remove(self.inicio.anterior.anterior)

    def removeNaPosicao(self, posicao: int) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')

        noAntecessor = self.inicio
        if posicao > 0:
            for i in range(posicao):
                noAntecessor = noAntecessor.proximo
                if noAntecessor.proximo == self.inicio:
                    noAntecessor.proximo
        elif posicao < 0:
            for i in range(0, posicao, -1):
                noAntecessor = noAntecessor.anterior
                if noAntecessor.anterior == self.incio:
                    noAntecessor = noAntecessor.anterior

        self._remove(noAntecessor)

    def exibe(self) -> None:
        print('Lista: inicio --> [', end='')
        if not self.estaVazia():
            p = self.inicio.proximo
            while p != self.inicio:
                print(p.elemento.valor, end='')
                if p.proximo != self.inicio:
                    print(', ', end='')
                p = p.proximo
        print(']')

    def esvazia(self):
        self.inicio.proximo = self.inicio
        self.inicio.anterior = self.inicio    