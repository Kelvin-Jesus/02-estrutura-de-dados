from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Item:
    valor: int

@dataclass
class No:
    elemento: Item
    filhoEsquerdo: No | None = None
    filhoDireito: No | None = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz: No | None = None

    def estaVazia(self) -> bool:
        return self.raiz is None

    def insereNaRaiz(self, elemento: Item) -> bool:
        if self.estaVazia():
            self.raiz = No(elemento)
            return True

        return False

    def insereNaEsquerda(self, elemento: Item, noPai: No) -> No | None:
        if noPai.filhoEsquerdo is None:
            noPai.filhoEsquerdo = No(elemento)
            return noPai.filhoEsquerdo

        return None

    def insereNaDireita(self, elemento: Item, noPai: No) -> No | None:
        if noPai.filhoDireito is None:
            noPai.filhoDireito = No(elemento)
            return noPai.filhoDireito

        return None

    def exibe(self) -> None:
        self._exibeNo(self.raiz)

    def _exibeNo(self, raizDaSubarvore: No) -> None:
        if raizDaSubarvore is None:
            return ''

        print('(', end='')
        self._exibeNo(raizDaSubarvore.filhoEsquerdo)

        print(f' {raizDaSubarvore.elemento.valor} ', end='')

        self._exibeNo(raizDaSubarvore.filhoDireito)
        print(')', end='')

    def buscarNo(self, elemento: Item) -> No | ValueError | None:
        if self.estaVazia():
            return ValueError('Árvore está vazia!')

        return self._buscarNo(elemento, self.raiz)

    def _buscarNo(self, elemento: Item, raiz: No) -> No | None:
        if raiz is None:
            return None

        if raiz.elemento.valor == elemento.valor:
            return raiz

        noBuscado = self.buscarNo(elemento, raiz.filhoEsquerdo)
        if noBuscado is not None:
            return noBuscado

        return self.buscarNo(elemento, raiz.filhoDireito)

a = ArvoreBinaria()
a.insereNaRaiz(Item(1))
a.insereNaDireita(Item(3), a.raiz)
a.insereNaEsquerda(Item(2), a.raiz)
a.insereNaEsquerda(Item(4), a.raiz.filhoEsquerdo)
a.insereNaDireita(Item(5), a.raiz.filhoEsquerdo)

a.exibe()
print("\n",a.buscarNo(Item(1)))
