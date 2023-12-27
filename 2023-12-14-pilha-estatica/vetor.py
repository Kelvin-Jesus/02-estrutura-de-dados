class Vetor():
    """Representa um vetor."""

    def __init__(self, tamanho: int, valorPreenchimento = None) -> None:
        """
		tamanho é a quantidade de elementos do vetor.
        valorPreenchimento é usado para inicializar cada posição.
		"""
        self.itens = list()
        for count in range(tamanho):
            self.itens.append(valorPreenchimento)

    def __len__(self) -> int:
        """-> Tamanho do vetor."""
        return len(self.itens)

    def __str__(self) -> str:
        """-> Representação string do vetor."""
        return str(self.itens)

    def __iter__(self):
        """Suporta a iteração pelos itens do vetor."""
        return iter(self.itens)

    def __getitem__(self, indice):
        """Operador de acesso aos elementos do vetor usando o índice"""
        if indice < 0 or indice >= len(self.itens):
            raise IndexError('Indice fora do limite')
        return self.itens[indice]

    def __setitem__(self, indice, novoItem):
        """Operador de substituição de um elemento usando o índice."""
        if indice < 0 or indice >= len(self.itens):
            raise IndexError('Indice fora do limite')
        self.itens[indice] = novoItem