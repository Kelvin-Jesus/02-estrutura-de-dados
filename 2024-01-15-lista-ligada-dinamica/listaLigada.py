from __future__ import annotations
from dataclasses import dataclass
import gc

@dataclass
class Item:
    valor: str

@dataclass
class No:
    elemento: Item
    proximo: No | None = None

class ListaLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None

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

