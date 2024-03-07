from __future__ import annotations
from enum import Enum

from Pessoa import Pessoa
from arvoreAVL import AVL

class Opcao(Enum):
    CADASTRO: int = 1
    BUSCA: int = 2
    RELATORIO: int = 3
    SAIR: int = 4

class CadastroDePessoa:
    def __init__(self) -> None:
        self.arvore = AVL()
    
    def escolherOpcao(self) -> int:
        print("="*50)
        print("Opções:\n")
        print("1 - CADASTRO")
        print("2 - BUSCA")
        print("3 - RELATORIO")
        print("4 - SAIR")
        print("="*50, end="\n")
        
        opcao = int(input("\nDigite a opção desejada: "))
        print("\n")

        return opcao
    
    def escolherOpcaoCadastro(self) -> None:
        print("="*50)
        print("Opções:\n")
        print("1 - Cadastrar UMA Pessoa")
        print("2 - Cadastrar Em Lote")
        print("="*50)

        opcao = int(input("\nDigite a opção desejada: "))
        print("")

        return opcao
    
    def criarNovaPessoa(self) -> Pessoa:
        nome = input("Digite o nome: ")
        nome = nome.lower()
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo: ")
        peso = float(input("Digite o peso: "))
        print("")

        return Pessoa(nome, idade, sexo, peso)
    
    def inserirPessoa(self, pessoa: Pessoa) -> None:
        if self.arvore.busca(pessoa) is None:
            print("Pessoa já cadastrada!")
            return

        self.arvore.insere(pessoa)
        print(f"{pessoa.nome} cadastrado(a) com sucesso!")

    def criarPessoasEmLote(self) -> None:
        pessoas = input("Digite a string contendo os dados das pessoas separados por \"|\": ")

        pessoas = pessoas.split("|")
        pessoas = [pessoa.split(",") for pessoa in pessoas]

        for pessoa in pessoas:
            nomeMinusculo = pessoa[0].lower()
            pessoa = Pessoa(nomeMinusculo, int(pessoa[1]), pessoa[2], float(pessoa[3]))
            self.inserirPessoa(pessoa)

    def encontrarPessoa(self) -> None:
        if self.arvore.vazia():
            print("Nenhuma pessoa cadastrada!")
            return

        nome = input("Digite o nome da pessoa que deseja buscar: ")
        nome = nome.lower()
        noDaPessoaBuscada = self.arvore.busca(Pessoa(nome, 0, "", 0))
        pessoa = noDaPessoaBuscada.elemento

        if noDaPessoaBuscada is not None:
            print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Sexo: {pessoa.sexo} | Peso: {pessoa.peso}\n")
        else:
            print(f"{nome} não encontrado(a)!\n")

    def exibeRelatorio(self) -> None:
        if self.arvore.vazia():
            print("Nenhuma pessoa cadastrada!")
            return

        listaDePessoas: list  = self._listaDePessoasEmOrdemAlfabetica()
        quantidadeDePessoas: int = len(listaDePessoas) 

        print("Pessoas em ordem alfabética: ", [pessoa.nome for pessoa in listaDePessoas])
        print("Quantidade de Pessoas cadastradas: ", quantidadeDePessoas)
        print("Quantidade de homens: ", len([pessoa for pessoa in listaDePessoas if pessoa.sexo == "m"]))
        print("Quantidade de mulheres: ", len([pessoa for pessoa in listaDePessoas if pessoa.sexo == "f"]))
        print("Peso médio das pessoas: ", round(sum([pessoa.peso for pessoa in listaDePessoas])/quantidadeDePessoas, ndigits=2))
        print("Quantidade de pessoas com mais de 18 anos: ", len([pessoa for pessoa in listaDePessoas if pessoa.idade > 18]), end="\n\n")

    def _listaDePessoasEmOrdemAlfabetica(self) -> list[Pessoa]:
        listaDePessoasNaArvore = []
        self.arvore.percorreEmOrdem(self.arvore.raiz, listaDePessoasNaArvore)

        return listaDePessoasNaArvore


def iniciarCadastroDePessoa() -> None:
        opcaoAtual = None
        simulador = CadastroDePessoa()

        while True:
            opcaoAtual = simulador.escolherOpcao()

            if opcaoAtual == Opcao.CADASTRO.value:
                opcaoCadastro = simulador.escolherOpcaoCadastro()

                if opcaoCadastro == 1:
                    pessoa = simulador.criarNovaPessoa()
                    simulador.inserirPessoa(pessoa)
                    print("")

                elif opcaoCadastro == 2:
                    simulador.criarPessoasEmLote()
                    print("")

                else:
                    print("Opção inválida, tente novamente.\n")
                    continue

            elif opcaoAtual == Opcao.BUSCA.value:
                simulador.encontrarPessoa()

            elif opcaoAtual == Opcao.RELATORIO.value:
                simulador.exibeRelatorio()

            elif opcaoAtual == Opcao.SAIR.value:
                print("Saindo...")
                break

            else:
                print("Opção inválida, tente novamente.\n")
                iniciarCadastroDePessoa()
            
iniciarCadastroDePessoa()
