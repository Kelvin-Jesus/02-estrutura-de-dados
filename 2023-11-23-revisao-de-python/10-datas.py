# Projete uma classe (dataclass) para representar uma data
# com dia, mês e ano. Em seguida:
# a) Projete uma função que verifique se uma data é o último dia do ano.
# b) Projete uma função que verifique se uma data é válida, considerando:
#   - 0 < ano < 9999 e 0 < mês < 13
#   - Meses 1, 3, 5, 7, 8, 10, 12 → 31 dias; meses 4, 6, 9, 11 → 30 dias;
#     mês 2 → 28 dias
# c) Projete uma função que receba duas datas e produza verdadeiro se a
# primeira vem antes que a segunda.

from dataclasses import dataclass

@dataclass
class Data:
    dia: int
    mes: int
    ano: int

def ehUltimoDiaDoAno(data: Data) -> bool:
    """
        >>> ehUltimoDiaDoAno(Data(dia=31, mes=12, ano=2021))
        True
        >>> ehUltimoDiaDoAno(Data(dia=20, mes=2, ano=2001))
        False
    """
    if data.dia == 31 and data.mes == 12:
        return True
    
    return False

def dataEhValida(data: Data) -> bool:
    """
        >>> dataEhValida(Data(dia=29, mes=11, ano=2023))
        True
        >>> dataEhValida(Data(dia=-1, mes=15, ano=9999))
        False
        >>> dataEhValida(Data(dia=31, mes=4, ano=2005))
        False
        >>> dataEhValida(Data(dia=30, mes=3, ano=2005))
        True
        >>> dataEhValida(Data(1, 1, 2024))
        True
        >>> dataEhValida(Data(28, 2, 1974))
        True
        >>> dataEhValida(Data(31, 10, 2004))
        True
        >>> dataEhValida(Data(31, 4, 2004))
        False
        >>> dataEhValida(Data(30, 3, 20000))
        False
        >>> dataEhValida(Data(31, 11, 2023))
        False
        >>> dataEhValida(Data(1, 12, 0))
        False
    """
    ANO_MAXIMO = 9999
    ANO_MINIMO = 1
    MESES_COM_31_DIAS = [ 1, 3, 5, 7, 8, 10, 12 ]

    if (data.ano < ANO_MINIMO or data.ano > ANO_MAXIMO) or (data.mes < 1 or data.mes > 12):
        return False
    
    if data.dia == 31 and data.mes not in MESES_COM_31_DIAS:
        return False
        
    if data.mes == 2 and data.dia > 28:
        return False
    
    return True

def vemAntes(dataInicial: Data, dataFinal: Data) -> bool:
    """
        Verifica se a data *d1* vem antes de *d2*.
        Retorna False se *d1* == *d2*.
        Exemplos
        >>> vemAntes(Data(31, 10, 2023), Data(15, 12, 2023))
        True
        >>> vemAntes(Data(31, 10, 2023), Data(1, 1, 2024))
        True
        >>> vemAntes(Data(1, 1, 2024), Data(31, 12, 2023))
        False
        >>> vemAntes(Data(1, 2, 2025), Data(1, 1, 2024))
        False
    """
    dataInicial = dataInicial.ano * 10000 + dataInicial.mes * 100 + dataInicial.dia
    dataFinal = dataFinal.ano * 10000 + dataFinal.mes * 100 + dataFinal.dia

    return dataInicial < dataFinal