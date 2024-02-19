from __future__ import annotations
from dataclasses import dataclass
from time import sleep

@dataclass
class Item:
    valor: str


@dataclass
class No:
    elemento: Item | None = None
    proximo: No | None = None

class ListaLigadaComSentinela:

    def __init__(self) -> None:
        self.inicio = No(None)
        self.fim = self.inicio

    def estaVazia(self) -> bool:
        return self.inicio.proximo == None

    def tamanho(self) -> int:
        noAtual = self.inicio.proximo
        tamanhoDaLista = 0

        while noAtual != None:
            tamanhoDaLista += 1
            noAtual = noAtual.proximo

        return tamanhoDaLista
    
    def exibe(self) -> None:
        print('Lista: inicio --> [', end='')
        elementoAtual = self.inicio.proximo

        while elementoAtual != None:
            print(elementoAtual.elemento, end='')
            elementoAtual = elementoAtual.proximo

            if elementoAtual != None:
                print(', ', end='')

        print('] <-- fim')

    def esvazia(self) -> None:
        self.inicio = self.inicio
        self.fim = self.inicio

    def busca(self, elemento: Item) -> No | None:
        elementoAtual = self.inicio.proximo

        while elementoAtual != None and elementoAtual.elemento.valor != elemento.valor:
            elementoAtual = elementoAtual.proximo

        return elementoAtual
    
    def buscaNaPosicao(self, posicao: int) -> No | None:
        if posicao < 0 or posicao > self.tamanho():
            raise ValueError('Posição Inválida')

        i = 0
        elementoAtual = self.inicio
        while elementoAtual != None and i < posicao:
            i += 1
            elementoAtual = elementoAtual.proximo

        return elementoAtual
        
    def insereNoFim(self, elemento: Item) -> None:
        if self.busca(elemento) != None:
            raise ValueError('Elemento repetido')

        novoNo = No(elemento)
        self.fim.proximo = novoNo
        self.fim = novoNo

    def insereNoInicio(self, elemento: Item) -> None:
        if self.busca(elemento) != None:
            raise ValueError('Elemento repetido')

        novoNo = No(elemento)
        if self.estaVazia():
            self.fim = novoNo
    
        novoNo.proximo = self.inicio.proximo
        self.inicio.proximo = novoNo

    def insereNaPosicao(self, elemento: Item, posicao: int) -> None:
        if self.busca(elemento) != None:
            raise ValueError('Elemento repetido')

        tamanhoDaLista = self.tamanho()
        if posicao < 0 or posicao > tamanhoDaLista:
            raise ValueError('Posição Inválida')

        if posicao == tamanhoDaLista:
            return self.insereNoFim(elemento)

        i = 0
        elementoAtual = self.inicio
        while elementoAtual != None and i < posicao:
            i += 1
            elementoAtual = elementoAtual.proximo

        novoNo = No(elemento)
        novoNo.proximo = elementoAtual.proximo
        elementoAtual.proximo = novoNo

    def removeNoInicio(self, elemento: Item) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')

        noRemovido = self.inicio.proximo
        self.inicio.proximo = noRemovido.proximo

        if self.estaVazia():
            self.fim = self.inicio

        noRemovido.proximo = None

    def removeNoFim(self) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')
        
        noAnterior = self.inicio
        noAtual = self.inicio.proximo

        while noAtual != self.fim:
            noAnterior = noAtual
            noAtual = noAtual.proximo

        noAnterior.proximo = noAtual.proximo
        self.fim = noAnterior

    def removeNaPosicao(self, posicao: int) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')

        tamanhoDaLista = self.tamanho()
        if posicao < 1 or posicao >= tamanhoDaLista:
            raise ValueError('Posição inválida')

        if posicao == (tamanhoDaLista - 1):
            return self.removeNoFim()

        i = 0
        noAnterior = self.inicio
        noAtual = self.inicio.proximo

        while noAtual != None and i < posicao:
            i += 1
            noAnterior = noAtual
            noAtual = noAtual.proximo

        noAnterior.proximo = noAtual.proximo
        noAtual.proximo = None

    def removeElemento(self, elemento: Item) -> None:
        if self.estaVazia():
            raise ValueError('Lista vazia')

        noRemovido = self.busca(elemento)
        if noRemovido == self.fim:
            return self.removeNoFim()

        noAnterior = self.inicio
        noAtual = self.inicio.proximo

        while noAtual != noRemovido:
            noAnterior = noAtual
            noAtual = noAtual.proximo

        noAnterior.proximo = noAtual.proximo
        noAtual.proximo = None

