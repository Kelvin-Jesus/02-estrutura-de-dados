from __future__ import annotations
from enum import Enum

from TabelaHash import TabelaHash

class Opcao(Enum):
    ARMAZENAR: int = 1
    CONSULTAR: int = 2
    RELATORIO: int = 3
    SAIR: int = 4

class ContadorDePalavras:
    def __init__(self):
        self.tabelaHash = TabelaHash(7)

    def escolherOpcao(self) -> int:
        print("="*50)
        print("Opções:\n")
        print("1 - ARMAZENAR")
        print("2 - CONSULTAR")
        print("3 - RELATORIO")
        print("4 - SAIR")
        print("="*50, end="\n")

        opcao = int(input("\nDigite a opção desejada: "))
        print("\n")

        return opcao

    def armazenar(self, palavra: str) -> None:
            self.tabelaHash.insere(palavra)

    def consultar(self, palavra: str):
        frequenciaPalavra = self.tabelaHash.quantidadeDeVezesQuePalavraAparece(palavra)
        if frequenciaPalavra == 0:
            print(f"A palavra '{palavra}' nao foi encontrada na tabela")
            return
        
        print(f"A palavra '{palavra}' aparece {frequenciaPalavra} vezes na tabela")
    

def iniciarFrequenciaDePalavras() -> None:
        opcaoAtual = None
        simulador = ContadorDePalavras()

        while True:
            opcaoAtual = simulador.escolherOpcao()

            if opcaoAtual == Opcao.ARMAZENAR.value:
                texto = input("Digite o texto: ")
                palavras = texto.lower().split()

                for palavra in palavras:
                    simulador.armazenar(palavra)

            elif opcaoAtual == Opcao.CONSULTAR.value:
                    palavraAhSerBuscada = input("Digite uma palavvra para buscar na tabela: ")
                    simulador.consultar(palavraAhSerBuscada)

            elif opcaoAtual == Opcao.RELATORIO.value:
                    simulador.tabelaHash.exibir()

            elif opcaoAtual == Opcao.SAIR.value:
                print("Saindo...")
                break

            else:
                print("Opção inválida, tente novamente.\n")
                iniciarFrequenciaDePalavras()

iniciarFrequenciaDePalavras()