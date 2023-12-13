from __future__ import annotations
from math import lcm

class Fracao:

    def __init__(self, numerador: int, denominador: int) -> None:
        self.numerador = numerador
        self.denominador = denominador

    def retornaValorReal(self) -> float:
        """
        >>> fracao = Fracao(1, 2)
        >>> fracao2 = Fracao(10, 10)
        >>> fracao.retornaValorReal()
        0.5
        >>> fracao2.retornaValorReal()
        1.0
        """
        return self.numerador / self.denominador

    def somaFracao(self, fracao: Fracao) -> Fracao:
        """
        >>> fracao1 = Fracao(10, 10)
        >>> fracao2 = Fracao(5, 5)
        >>> fracao1.somaFracao(fracao2).retornaValorReal()
        2.0
        >>> fracao2.somaFracao(fracao1).retornaValorReal()
        2.0
        """
        denominadoresSaoDiferentes: bool = self.denominador != fracao.denominador
        numerador = self.numerador + fracao.numerador
        denominadorComum = self.denominador

        if ( denominadoresSaoDiferentes ):
            denominadorComum = lcm(self.denominador, fracao.denominador)
            numerador1Transformado = (denominadorComum / self.denominador) * self.denominador
            numerador2Transformado = (denominadorComum / fracao.denominador) * fracao.denominador
            numerador = numerador1Transformado + numerador2Transformado
        
        return Fracao(numerador, denominadorComum)
    
    def subtraiFracao(self, fracao: Fracao) -> Fracao:
        """
        >>> fracao1 = Fracao(10, 2)
        >>> fracao2 = Fracao(5, 2)
        >>> fracao1.subtraiFracao(fracao2).retornaValorReal()
        2.5
        >>> fracao2.subtraiFracao(fracao1).retornaValorReal()
        -2.5
        """
        denominadoresSaoDiferentes: bool = self.denominador != fracao.denominador
        numerador = self.numerador - fracao.numerador
        denominadorComum = self.denominador

        if ( denominadoresSaoDiferentes ):
            denominadorComum = lcm(self.denominador, fracao.denominador)
            numerador1Transformado = (denominadorComum / self.denominador) * self.denominador
            numerador2Transformado = (denominadorComum / fracao.denominador) * fracao.denominador
            numerador = numerador1Transformado - numerador2Transformado
        
        return Fracao(numerador, denominadorComum)
    
    def divideFracao(self, fracao: Fracao) -> Fracao:
        """
        >>> fracao1 = Fracao(10, 2)
        >>> fracao2 = Fracao(5, 2)
        >>> fracao1.divideFracao(fracao2).retornaValorReal()
        2.0
        >>> fracao2.divideFracao(fracao1).retornaValorReal()
        0.5
        """
        fracaoInvertida = Fracao(fracao.denominador, fracao.numerador) 

        return self.multiplicaFracao(fracaoInvertida)
    
    def multiplicaFracao(self, fracao: Fracao) -> Fracao:
        """
        >>> fracao1 = Fracao(10, 2)
        >>> fracao2 = Fracao(5, 2)
        >>> fracao1.multiplicaFracao(fracao2).retornaValorReal()
        12.5
        >>> fracao2.multiplicaFracao(fracao1).retornaValorReal()
        12.5
        """
        numerador = self.numerador * fracao.numerador
        denominador = self.denominador * fracao.denominador

        return Fracao(numerador, denominador)
    
    def __str__(self):
        return f"({self.numerador}/{self.denominador})"
