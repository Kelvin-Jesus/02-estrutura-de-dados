from copy import deepcopy
from dataclasses import dataclass
from __future__ import annotations
from vetor import Vetor

@dataclass
class Item:
    valor: str

class ListaEstatica:

    def __init__(self, tamanhoMaximo: int) -> None:
        self.TAMANHO_MAXIMO = tamanhoMaximo
        self.elementos = Vetor(tamanhoMaximo)
        self.fim = 0

    def tamanho(self) -> int:
        return self.fim
    
    def estaVazia(self) -> bool:
        return self.fim == 0
    
    def estaCheia(self) -> bool:
        return self.fim == self.TAMANHO_MAXIMO
    
    def primeiro(self) -> Item:
        if self.estaVazia():
            raise ValueError('Lista esá vazia')

        return deepcopy(self.elementos[0])