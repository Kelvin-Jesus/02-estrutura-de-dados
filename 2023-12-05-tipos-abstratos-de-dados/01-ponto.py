from __future__ import annotations
from math import sqrt, pow

class Ponto:
    
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def acessa(self) -> tuple:
        """
        >>> p = Ponto(10, 20)
        >>> p.acessa()
        (10, 20)
        """
        return (self.x, self.y)
    
    def atribui(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distancia(self, ponto: Ponto) -> float:
        """
        >>> p1 = Ponto(10, 20)
        >>> p2 = Ponto(10, 11)
        >>> p1.distancia(p2)
        9.0
        """
        diffDeX1AteX2AoQuadrado = pow(self.x - ponto.x, 2)
        diffDeY1AteY2AoQuadrado = pow(self.y - ponto.y, 2)

        return sqrt(diffDeX1AteX2AoQuadrado + diffDeY1AteY2AoQuadrado)