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

    def insere(self, valor: int, raiz: No | None = None) -> No | None:
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

    def busca(self, valor: int) -> No | None:
        return self._busca(valor, self.raiz)

    def _busca(self, valor: int, raiz: No | None) -> No | None:
        if raiz is None or valor == raiz.valor:
            return raiz
        
        if valor > raiz.valor:
            return self._busca(valor, raiz.filhoDireito)

        return self._busca(valor, raiz.filhoEsquerdo)

    def remove(self, valor: int) -> None:
        self.raiz = self._removeNo(valor, self.raiz)

    def _removeNo(self, valor: int, raiz: No | None) -> No | None:
        if raiz is None:
            return raiz

        if valor < raiz.valor:
            raiz.filhoEsquerdo = self._removeNo(valor, raiz.filhoEsquerdo)
            return raiz
        
        if valor > raiz.valor:
            raiz.filhoDireito = self._removeNo(valor, raiz.filhoDireito)
            return raiz

        # raiz tem dois filhos
        if raiz.filhoEsquerdo is not None and raiz.filhoDireito is not None:
            self._trocaSucessor(raiz)
            raiz.filhoDireito = self._removeNo(valor, raiz.filhoDireito)

            return raiz

        # raiz tem apenas um filho ou é folha 
        if raiz.filhoEsquerdo is not None:
            raiz = raiz.filhoEsquerdo
            return raiz

        raiz = raiz.filhoDireito
        return raiz

    def _trocaSucessor(self, no: No | None) -> None:
        sucessor = no.filhoDireito
        while (sucessor.filhoEsquerdo is not None):                
            sucessor = sucessor.filhoEsquerdo
            no.valor, sucessor.valor = sucessor.valor, no.valor

    def altura(self, raiz: No | None) -> int:
	    if raiz is None:
	    	return -1

	    alturaSubArvoreDireita = 1 + self.altura(raiz.filhoDireito)
	    alturaSubArvoreEsquerda = 1 + self.altura(raiz.filhoEsquerdo)

	    if alturaSubArvoreDireita > alturaSubArvoreEsquerda:
		    return alturaSubArvoreEsquerda

	    return alturaSubArvoreEsquerda

    def percorrerEmInOrdem(self, raiz: No) -> None:
	    if raiz == None:
		    return None

	    self.percorrerEmInOrdem(raiz.filhoEsquerdo)
	    print(raiz.valor, ' ', end='')
	    self.percorrerEmInOrdem(raiz.filhoDireito)

    def exibe(self, raiz: No | None) -> None:
        if self.raiz is None or raiz is None:
            return None
        
        print("(", end='')
        self.exibe(raiz.filhoEsquerdo)
        print(f' {raiz.valor} ', end='')
        self.exibe(raiz.filhoDireito)
        print(")", end='')


a = ArvoreBinariaDeBusca()
a.insere(4)
a.insere(2)
a.insere(3)
a.insere(1)
a.insere(6)
a.insere(5)
a.insere(7)
a.exibe(a.raiz)

no = a.busca(7)
if no != None:
    print(no.valor)
else: 
    print(no)

print('Altura da ABB a =', a.altura(a.raiz))
print('Percurso da ABB a em in-ordem:')
a.percorrerEmInOrdem(a.raiz)

a.remove(7)
a.exibe(a.raiz)
a.remove(4)
a.exibe(a.raiz)
