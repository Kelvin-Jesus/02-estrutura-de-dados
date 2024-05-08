from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    valor: int 
    filhoEsquerdo: No | None = None
    filhoDireito: No | None = None

class ArvoreBinariaDeBusca:
    def __init__(self) -> None:
        self.raiz: No | None = None

    def insere(self, valor: int | str, raiz: No | None = None) -> No | None:
        if self.raiz is None:
            self.raiz  = No(valor)
            return self.raiz

        if raiz is None:
            return No(valor)

        if valor < raiz.valor:
            raiz.filhoEsquerdo = self.insere(valor, raiz.filhoEsquerdo)
        
        else:
            raiz.filhoDireito = self.insere(valor, raiz.filhoDireito)

        return raiz

    def exibe(self, raiz: No | None) -> None:
        if self.raiz is None or raiz is None:
            return None
        
        print("(", end='')
        self.exibe(raiz.filhoEsquerdo)
        print(f' {raiz.valor} ', end='')
        self.exibe(raiz.filhoDireito)
        print(")", end='')

abb = ArvoreBinariaDeBusca()
abb.insere(4, None)
abb.insere(2, abb.raiz)
abb.insere(3, abb.raiz)
abb.insere(1, abb.raiz)
abb.insere(6, abb.raiz)
abb.insere(5, abb.raiz)
abb.insere(7, abb.raiz)
abb.exibe(abb.raiz)
