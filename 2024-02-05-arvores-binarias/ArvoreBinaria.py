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
        self.raiz = None

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
            return None

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

        noBuscado: No | None = self.buscarNo(elemento, raiz.filhoEsquerdo)
        if noBuscado is not None:
            return noBuscado

        return self.buscarNo(elemento, raiz.filhoDireito)

    def altura(self, raiz: No) -> int:
        if raiz == None:
            return -1

        alturaSubArvoreDireita = 1 + self.altura(raiz.filhoDireito)
        alturaSubArvoreEsquerda = 1 + self.altura(raiz.filhoEsquerdo)

        if alturaSubArvoreDireita > alturaSubArvoreEsquerda:
            return alturaSubArvoreEsquerda

        return alturaSubArvoreEsquerda

    def percorrerEmPreOrdem(self, raiz: No) -> None:
        if raiz == None:
            return None

        print(raiz.elemento.valor, ' ', end='')
        self.percorrerEmPreOrdem(raiz.filhoEsquerdo)
        self.percorrerEmPreOrdem(raiz.filhoDireito)

    def percorrerEmInOrdem(self, raiz: No) -> None:
        if raiz == None:
            return None

        self.percorrerEmInOrdem(raiz.filhoEsquerdo)
        print(raiz.elemento.valor, ' ', end='')
        self.percorrerEmInOrdem(raiz.filhoDireito)

    def percorrerEmPosOrdem(self, raiz: No) -> None:
        if raiz == None:
            return None

        self.percorrerEmPosOrdem(raiz.filhoEsquerdo)
        self.percorrerEmPosOrdem(raiz.filhoDireito)
        print(raiz.elemento.valor, ' ', end='')

