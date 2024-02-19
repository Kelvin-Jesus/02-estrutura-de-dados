from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Item:
    valor: str

@dataclass
class No:
    elemento: Item
    proximo: No | None = None

class ListaLigada:

    def __init__(self):
        self.inicio: No | None = None
        self.fim: No | None = None

    def estaVazia(self) -> bool:
        return self.inicio == None

    def tamanho(self) -> int:
        elementoAtual = self.inicio
        tamanho = 0

        while elementoAtual != None:
            tamanho += 1
            elementoAtual = elementoAtual.proximo

        return tamanho

    def exibe(self) -> None:
        print('Lista: inicio --> [', end='')
        elementoAtual = self.inicio

        while elementoAtual != None:
            print(elementoAtual.elemento.valor, end='')
            elementoAtual = elementoAtual.proximo

            if elementoAtual != None:
                print(', ', end='')

        print('] <-- fim')

    def esvazia(self) -> None:
        self.inicio = None
        self.fim = None

    def busca(self, elemento: Item) -> No | None:
        elementoAtual = self.inicio

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
        if self.estaVazia():
            self.inicio = novoNo
        else:
            self.fim.proximo = novoNo

        self.fim = novoNo

    def insereNoInicio(self, elemento: Item) -> None:
        if self.busca(elemento) != None:
            raise ValueError('Elemento Repetido')

        novoNo = No(elemento)
        if self.estaVazia():
            self.fim = novoNo

        novoNo.proximo = self.inicio
        self.inicio = novoNo

    def insereNaPosicao(self, elemento: Item, posicao: int) -> None:
        if self.busca(elemento) != None:
            raise ValueError('Elemento Repetido')

        tamanhoDaLista = self.tamanho()
        if posicao < 0 or posicao > tamanhoDaLista:
            raise ValueError('Posição Inválida')
        
        if posicao == 0:
            self.insereNoInicio(elemento)
        elif posicao == tamanhoDaLista:
            self.insereNoFim(elemento)
        else:
            i = 1
            elementoAtual = self.inicio.proximo
            
            while elementoAtual != None and i < (posicao - 1):
                i += 1
                elementoAtual = elementoAtual.proximo

            novoNo = No(elemento)
            novoNo.proximo = elementoAtual.proximo
            elementoAtual.proximo = novoNo

    def removeNoInicio(self) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')
        
        noRemovido = self.inicio
        self.inicio = self.inicio.proximo
        if self.estaVazia():
            self.fim = None

        noRemovido.proximo = None

    def removeNoFim(self) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')

        if self.tamanho() == 1:
            self.inicio = None
            self.fim = None
        else:
            elementoAtual = self.inicio
            elementoAnterior = None

            while elementoAtual != self.fim:
               elementoAnterior = elementoAtual
               elementoAtual = elementoAtual.proximo

            elementoAnterior.proximo = None
            self.fim = elementoAnterior

    def removeNaPosicao(self, posicao: int) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')
        
        tamanhoDaLista = self.tamanho()
        if posicao < 0 or posicao > tamanhoDaLista:
            raise ValueError('Posição Inválida')

        if posicao == 0:
            return self.removeNoInicio()

        if posicao == (tamanhoDaLista - 1):
            return self.removeNoFim()

        i = 1
        elementoAnterior = self.inicio
        elementoAtual = self.inicio.proximo

        while elementoAtual != None and i < posicao:
            elementoAnterior = elementoAtual
            elementoAtual = elementoAtual.proximo
            i += 1

        elementoAnterior.proximo = elementoAtual.proximo
        elementoAtual.proximo = None

    def removeElemento(self, elemento: Item) -> None:
        if self.estaVazia():
            raise ValueError('Lista Vazia')

        noRemovido = self.busca(elemento)
        if noRemovido == self.inicio:
            return self.removeNoInicio()

        if noRemovido == self.fim:
            return self.removeNoFim()

        noAnterior = self.inicio
        noAtual = self.inicio.proximo

        while noAtual != noRemovido:
            noAnterior = noAtual
            noAtual = noAtual.proximo

        noAnterior.proximo = noAtual.proximo
        noAtual.proximo = None
