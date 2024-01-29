from enum import Enum
from Fila import Fila
from Cliente import Cliente, TipoDeCliente

filaPreferencial = Fila(20)
filaComum = Fila(20)

class Opcao(Enum):
    GERAR_SENHA: int = 1
    CHAMAR_CLIENTE: int = 2
    CONSULTAR_CLIENTES_EM_ESPERA: int = 3
    CONSULTAR_ESTADO_DOS_CAIXAS: int = 4
    SAIR: int = 5

class Caixa:
    
    def __init__(self, numero: int):
        self.numero: int = numero
        self.clienteAtual: Cliente = None

class SimuladorDeCaixa:

    def __init__(self, numeroDeCaixas: int):
        self.numeroDeCaixas: int = numeroDeCaixas
        self.caixas: list = [Caixa(i+1) for i in range(numeroDeCaixas)]

    def gerarSenha(self) -> None:
        print("\nEscolha o tipo de cliente:")
        print("1 - Cliente Preferencial")
        print("2 - Cliente Comum", end="\n\n")
        tipoDeCliente = int(input("Digite o tipo de cliente: "))

        if tipoDeCliente != TipoDeCliente.PREFERENCIAL.value and tipoDeCliente != TipoDeCliente.COMUM.value:
            print("Tipo de cliente inválido, tente novamente.")
            self.gerarSenha()

        cliente = None

        if tipoDeCliente == TipoDeCliente.PREFERENCIAL.value:
            senha = "clientePreferencial-" + str(filaPreferencial.tamanho())
            cliente = Cliente("preferencial", senha)
            filaPreferencial.enfileira(cliente)
        else:
            senha = "clienteComum-" + str(filaComum.tamanho())
            cliente = Cliente("comum", senha)
            filaComum.enfileira(cliente)

        print(f"Senha gerada: {senha}", end="\n\n")


    def chamarCliente(self, numeroDoCaixa: int) -> None:
        fila = filaPreferencial if filaPreferencial.tamanho() > 0 else filaComum

        if fila.tamanho() == 0:
            print("Não há clientes em espera.")
            return
        
        clienteAtual = fila.desenfileira()
        caixa = self.caixas[numeroDoCaixa - 1]
        caixa.clienteAtual = clienteAtual

        print(f"Chamando cliente com a senha: \"{clienteAtual.senha}\" para o caixa: {caixa.numero}", end="\n\n")

    def consultarClientesEmEspera(self) -> None:
        print("\nClientes Preferenciais em espera:", end="\n")
        filaPreferencial.exibe()
        print("\n")

        print("Clientes Comuns em espera:", end="\n")
        filaComum.exibe()
        print("\n")

    def consultarEstadoDosCaixas(self) -> None:
        for caixa in self.caixas:
            print(f"Caixa {caixa.numero}: ", end="")

            if caixa.clienteAtual == None:
                print("Livre")
            else:
                print(f"Ocupado com o cliente de senha \"{caixa.clienteAtual.senha}\"")

        print("\n")

    def sair(self) -> None:
        print("Simulador encerrado!")

def printarOpcoes() -> None:
    print("\n")
    print("="*50)
    print("Opções:\n")
    print("1 - Gerar Senha")
    print("2 - Chamar Cliente")
    print("3 - Consultar clientes em espera")
    print("4 - Consultar estado dos caixas")
    print("5 - Sair")
    print("="*50, end="\n")

def iniciarSimulador(numeroDeCaixas: int) -> None:
    opcaoAtual = None

    simulador = SimuladorDeCaixa(numeroDeCaixas)

    while True:
        printarOpcoes()
        opcaoAtual = int(input("Digite a opção desejada: "))

        if opcaoAtual == Opcao.GERAR_SENHA.value:
            simulador.gerarSenha()
        elif opcaoAtual == Opcao.CHAMAR_CLIENTE.value:
            numeroDoCaixa = int(input("Digite o número do caixa: "))
            simulador.chamarCliente(numeroDoCaixa)
        elif opcaoAtual == Opcao.CONSULTAR_CLIENTES_EM_ESPERA.value:
            simulador.consultarClientesEmEspera()
        elif opcaoAtual == Opcao.CONSULTAR_ESTADO_DOS_CAIXAS.value:
            simulador.consultarEstadoDosCaixas()
        elif opcaoAtual == Opcao.SAIR.value:
            simulador.sair()
            break
        else:
            print("Opção inválida, tente novamente.\n")
            iniciarSimulador(numeroDeCaixas)

numeroDeCaixas = int(input("\nDigite o número de caixas(entre 2 e 20): "))

if numeroDeCaixas >= 2 and numeroDeCaixas <= 20:
    iniciarSimulador(numeroDeCaixas)
else: 
    print("Número de caixas inválido, tente novamente.")
