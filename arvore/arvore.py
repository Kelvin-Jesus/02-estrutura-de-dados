from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Item:
     valor: str | int | float

@dataclass
class No:
     elemento: Item
     filhoEsq: No | None = None
     filhoDir: No | None = None

class AB:
     " Representa uma árvore binária"
     def __init__(self):
          self.raiz: No | None = None

     def vazia(self):
          return self.raiz == None

     def insereRaiz(self, elem: Item) -> bool:
          if self.vazia():
               self.raiz = No(elem)
               return True
          return False
    
     def insereNaEsq(self, elem: Item, pai: No) -> bool:
          if pai.filhoEsq == None:
               pai.filhoEsq = No(elem)
               return True
          return False

     def insereNaDir(self, elem: Item, pai: No) -> bool:
          if pai.filhoDir == None:
               pai.filhoDir = No(elem)
               return True
          return False
    
     def exibe(self) -> None:
          self._exibeNo(self.raiz)
          print()
    
     def _exibeNo(self, raiz: No) -> None:
          if raiz != None:
               print('(', end='')
               self._exibeNo(raiz.filhoEsq)
               print(' ', raiz.elemento.valor, ' ', end='')
               self._exibeNo(raiz.filhoDir)
               print(')', end='')

     def busca(self, elem: Item) -> No | None:
          return self._buscaNo(elem, self.raiz)
    
     def _buscaNo(self, elem: Item, raiz: No) -> No | None:
          if raiz == None:
               return None
          
          if raiz.elemento.valor == elem.valor:
               return raiz
          no = self._buscaNo(elem, raiz.filhoEsq)
          if no != None:
               return no
          return self._buscaNo(elem, raiz.filhoDir)
       
     def insereNaEsquerda(self, elem: Item, elemPai: Item) -> bool:
          pai = self.busca(elemPai)
          if pai != None:
               return self.insereNaEsq(elem, pai)
          return False
    
     def insereNaDireita(self, elem: Item, elemPai: Item) -> bool:
          pai = self.busca(elemPai)
          if pai != None:
               return self.insereNaDir(elem, pai)
          return False
     
     def altura(self) -> int:
          if self.vazia():
               raise ValueError('Árvore vazia')
          return self._alturaNo(self.raiz)

     def _alturaNo(self, raiz: No) -> int:
          if raiz == None:
               return -1
          return 1 + max(self._alturaNo(raiz.filhoEsq), self._alturaNo(raiz.filhoDir))
     
     # valores de ordem: 0 = pré-ordem, 1 = in-ordem e 2 = pos-ordem
     def percorreArvore(self, ordem: int = 0) -> None:
          if ordem == 0:
               self._percorrePreOrdem(self.raiz)
          elif ordem == 1:
               self._percorreInOrdem(self.raiz)
          elif ordem == 2:
               self._percorrePosOrdem(self.raiz)
          else: 
               raise ValueError('Valor inválido para o parâmetro de ordem')
          print()
     
     def _percorrePreOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._visitaNo(raiz)
               self._percorrePreOrdem(raiz.filhoEsq)
               self._percorrePreOrdem(raiz.filhoDir)

     def _percorreInOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._percorreInOrdem(raiz.filhoEsq)
               self._visitaNo(raiz)
               self._percorreInOrdem(raiz.filhoDir)

     def _percorrePosOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._percorrePosOrdem(raiz.filhoEsq)
               self._percorrePosOrdem(raiz.filhoDir)
               self._visitaNo(raiz)

     def _visitaNo (self, no: No) -> None:
          print(no.elemento.valor, ' ', end='')
          