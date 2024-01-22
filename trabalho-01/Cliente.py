from enum import Enum                            

class TipoDeCliente(Enum):
    PREFERENCIAL: int = 1
    COMUM: int = 2

class Cliente:

    def __init__(self, tipo: TipoDeCliente, senha: str):
        self.tipo: TipoDeCliente = tipo
        self.senha: str = senha