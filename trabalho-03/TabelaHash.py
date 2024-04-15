from __future__ import annotations

class TabelaHash:
    def __init__(self, tamanho: int) -> None:
        self.tabela = [[] for _ in range(tamanho)]
        self.tamanhoMaximo = tamanho

    def insere(self, chave: str) -> None:
        hash = self._hash(chave)
        for indice, (palavra, quantidade) in enumerate(self.tabela[hash]):
            if palavra == chave:
                self.tabela[hash][indice] = (palavra, quantidade + 1)
                return

        self.tabela[hash].append((chave, 1))
        print("Inserido com sucesso!")

    def busca(self, chave: str) -> bool:
        indice = self._hash(chave)
        for palavra, _ in self.tabela[indice]:
            if palavra == chave:
                return True

        return False
    
    def _hash(self, chave: str) -> int:
        soma = 0
        indice = 0

        comprimento = len(chave)
        temComprimentoImpar = comprimento % 2 == 1
        if temComprimentoImpar:
            chave = chave + ' '
        
        while (indice < comprimento):
            soma += self.tamanhoMaximo*ord(chave[indice]) + ord(chave[indice + 1])
            soma = soma % 19937
            indice += 2

        return soma % self.tamanhoMaximo
    
    def exibir(self):
        for indice, lista in enumerate(self.tabela):
            print(f"Índice {indice}: {lista}")

    def quantidadeDeVezesQuePalavraAparece(self, chave: str) -> int:
        indice = self._hash(chave)
        for palavra, quantidade in self.tabela[indice]:
            if palavra == chave:
                return quantidade
        return 0
