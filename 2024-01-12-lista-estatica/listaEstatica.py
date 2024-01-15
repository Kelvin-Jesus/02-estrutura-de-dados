from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
from vetor import Vetor

@dataclass
class Item:
    valor: str

ERRO_LISTA_VAZIA = 'Lista está vazia'

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
    
    def esvazia(self) -> None:
        self.fim = 0
    
    def primeiro(self) -> Item:
        if self.estaVazia():
            raise ValueError(ERRO_LISTA_VAZIA)

        return deepcopy(self.elementos[0])
    
    def ultimo(self) -> Item:
        if self.estaVazia():
            raise ValueError(ERRO_LISTA_VAZIA)
    
    def exibe(self) -> None:
        print('Lista: inicio --> [', end='')

        for posicao in range(self.fim):
            print(self.elementos[posicao].valor, end='')

            if posicao < (self.fim - 1):
                print(', ', end='')

        print('] <-- fim')

    def buscar(self, elemento: Item) -> int:
        for posicao in range(self.fim):
            if self.elementos[posicao].valor == elemento.valor:
                return posicao
                
        return -1
    
    def buscaPosicao(self, posicao: int) -> Item:
        if self.estaVazia():
            raise ValueError(ERRO_LISTA_VAZIA)
            
        if posicao < 0 or posicao >= self.TAMANHO_MAXIMO:
            raise ValueError('Índice inválido')
            
        if posicao >= self.fim:
            raise ValueError('Posição inválida')

        return deepcopy(self.elementos[posicao])
    
    def insere(self, elemento: int) -> None:
        if self.estaCheia():
            raise ValueError('Lista está cheia')
            
        if self.buscar(elemento) >= 0:
            raise ValueError('Elemento repetido')
            
        self.elementos[self.fim] = deepcopy(elemento)
        self.fim += 1

    def _deslocaAhDireita(self, posicaoDoNovoElemento: int) -> None:
        for posicao in range(self.fim, posicaoDoNovoElemento, -1):
            self.elementos[posicao] = self.elementos[posicao - 1]

    def insereNaPosicao(self, elemento: Item, posicao: int) -> None:
        if self.estaCheia():
            raise ValueError('Lista está cheia')
            
        if self.buscar(elemento) >= 0:
            raise ValueError('Elemento repetido')
            
        if posicao < 0 or posicao >= self.TAMANHO_MAXIMO:
            raise ValueError('Índice inválido')
                
        if posicao >= self.fim:
            raise ValueError('Posição inválida')
            
        self._deslocaAhDireita(posicao)
        self.elementos[posicao] = deepcopy(elemento)
        self.fim += 1
    
    def remove(self) -> None:
        if self.estaVazia():
            raise ValueError('Lista está vazia')
            
        self.fim -= 1

    def _deslocaAhEsquerda(self, posicaoDoElemento: int) -> None:
        for posicao in range(posicaoDoElemento + 1, self.fim):
            self.elementos[posicao - 1] = self.elementos[posicao]

    def removeNaPosicao(self, posicao: int) -> None:
        if self.estaVazia():
            raise ValueError('Lista está vazia')
            
        if posicao < 0 or posicao >= self.TAMANHO_MAXIMO:
            raise ValueError('Índice inválido')
                
        if posicao >= self.fim:
            raise ValueError('Posição inválida')
            
        self._deslocaAhEsquerda(posicao)
        self.fim -= 1

    def removeElemento(self, elemento: Item) -> None:
        if self.estaVazia():
            raise ValueError('Lista está vazia')
            
        posicaoDoElemento = self.buscar(elemento)
        if posicaoDoElemento == -1:
            raise ValueError('Elemento inexistente')
            
        self._deslocaEsquerda(posicaoDoElemento)
        self.fim -= 1