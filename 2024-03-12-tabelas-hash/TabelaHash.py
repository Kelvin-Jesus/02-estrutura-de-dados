from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass

@dataclass
class Pessoa:
    sobrenome: str
    nome: str
    idade: int = 0
    peso: float = 0

class TabelaHash:
    def __init__(self, tamanho: int) -> None:
        self.tabela = [None] * tamanho
        self.tamanhoMaximo = tamanho

    def insere(self, pessoa: Pessoa) -> None:
        indiceAhInserir = self._mapeia(pessoa.sobrenome)

        self.tabela[indiceAhInserir] = pessoa

    def busca(self, chave: Pessoa) -> None:
        indiceDaPessoa = self._mapeia(chave)

        return deepcopy(self.tabela[indiceDaPessoa])

    def _mapeia(self, chave: str) -> int:
        chave = chave.upper()

        soma = 0
        for letra in chave:
            soma += ord(letra)

        return soma % self.tamanhoMaximo
    
    def _hash(chave: str) -> int:
        soma = 0
        indice = 0

        comprimento = len(chave)
        temComprimentoImpar = comprimento % 2 == 1
        if temComprimentoImpar:
            chave = chave + ' '
        
        while (indice < comprimento):
            soma += 100*ord(chave[indice]) + ord(chave[indice + 1])
            soma = soma % 19937
            indice += 2

        return soma % 101


tabela = TabelaHash(100)
tabela.insere(Pessoa('Silva', 'João', 25))
tabela.insere(Pessoa('Freitas', 'Maria', 30))
tabela.insere(Pessoa('Flores', 'José', 40))
tabela.insere(Pessoa('Souza', 'Ana', 35))

pessoa = tabela.busca('Flores')
print(pessoa)