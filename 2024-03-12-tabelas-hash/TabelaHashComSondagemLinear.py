from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
from multiprocessing import Value

@dataclass
class Pessoa:
    sobrenome: str
    nome: str
    idade: int = 0
    peso: float = 0

class TabelaHashComSondagemLinear:
    NULO = None

    def __init__(self, tamanho: int)  -> None:
        self.tabela: int = [TabelaHashComSondagemLinear.NULO] * tamanho
        self.TAMANHO_MAXIMO: int = tamanho
        self.totalDeElementos: int = 0

    def estaCheia(self) -> bool:
        return self.total == self.TAMANHO_MAXIMO
    
    def _hash(self, chave: str) -> int:
        chave = chave.upper()

        soma = 0
        for letra in chave:
            soma += ord(letra)

        return soma % self.TAMANHO_MAXIMO
    
    def _rehash(self, indice: int) -> int:
        return (indice + 1) % self.TAMANHO_MAXIMO
    
    def insere(self, pessoa: Pessoa) -> None:
        if self.estaCheia():
            raise ValueError("Tabela Hash está cheia")
        
        indice = self._hash(pessoa.sobrenome)
        while self.tabela[indice] != TabelaHashComSondagemLinear.NULO:
            indice = self._rehash(indice)
        
        self.tabela[indice] = pessoa
        self.totalDeElementos += 1

    def busca(self, chave: str) -> Pessoa | None:
        sobrenome: str = chave.upper()
        indice: int = self._hash(sobrenome)

        indiceInicial: int = indice

        while self.tabela[indice] != TabelaHashComSondagemLinear.NULO:
            pessoa: Pessoa = self.tabela[indice]
            if pessoa.sobrenome == sobrenome:
                return pessoa
            
            indice = self._rehash(indice)
            if indice == indiceInicial:
                return None
            
        return None
