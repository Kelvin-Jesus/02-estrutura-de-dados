from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Item:
    chave: str
    valor: str = 0

class TabelaHashComSondagemLinear:
    NULO = None
    LAPIDE = True

    def __init__(self, tamanho: int)  -> None:
        self.tabela: int = [TabelaHashComSondagemLinear.NULO] * tamanho
        self.TAMANHO_MAXIMO: int = tamanho
        self.totalDeElementos: int = 0

    def estaCheia(self) -> bool:
        return self.totalDeElementos == self.TAMANHO_MAXIMO
    
    def _hash(self, chave: str) -> int:
        chave = chave.upper()

        soma = 0
        for letra in chave:
            soma += ord(letra)

        return soma % self.TAMANHO_MAXIMO
    
    def _rehash(self, indice: int) -> int:
        return (indice + 1) % self.TAMANHO_MAXIMO
    
    def insere(self, item: Item) -> None:
        if self.estaCheia():
            raise ValueError("Tabela Hash está cheia")
        
        indice = self._hash(item.chave.upper())
        while self.tabela[indice] != TabelaHashComSondagemLinear.NULO \
            and self.tabela[indice] != TabelaHashComSondagemLinear.LAPIDE:
            indice = self._rehash(indice)
        
        self.tabela[indice] = item
        self.totalDeElementos += 1

    def busca(self, chave: str) -> Item | None:
        sobrenome: str = chave.upper()
        indice: int = self._hash(sobrenome)

        indiceInicial: int = indice

        while self.tabela[indice] != TabelaHashComSondagemLinear.NULO:
            if self.tabela[indice] != TabelaHashComSondagemLinear.LAPIDE \
                and self.tabela[indice].chave.upper() == chave.upper():
                return self.tabela[indice]
            
            indice = self._rehash(indice)
            if indice == indiceInicial:
                return None
            
        return None
    
    def remove(self, chave: str) -> None:
        indice: int = self._hash(chave)
        indiceInicial: int = indice

        while self.tabela[indice] != TabelaHashComSondagemLinear.NULO:
            if self.tabela[indice] != TabelaHashComSondagemLinear.LAPIDE \
                and self.tabela[indice].chave.upper() == chave.upper():
                self.tabela[indice] = self.LAPIDE
                self.totalDeElementos -= 1

            else:
                indice = self._rehash(indice)
                if indice == indiceInicial:
                    return None
    
    def exibe(self) -> None:
        print('Indice\t Item')
        for i, p in enumerate(self.tabela):
            print(i, '\t', p)
        print('Tamanho da tabela =', self.TAMANHO_MAXIMO)
        print('Total de itens =', self.totalDeElementos)


def main():
    t = TabelaHashComSondagemLinear(5)
    t.insere(Item('Souza', 22))
    t.insere(Item('Freitas', 22))
    t.insere(Item('Flores', 22))
    t.insere(Item('Silva', 22))
    t.insere(Item('Noel', 22))

    t.remove('souza')

    t.insere(Item('Leon', 22))
    t.exibe()

    p = t.busca('leon')
    print(p)
    
    
if __name__ == "__main__":
    main()
