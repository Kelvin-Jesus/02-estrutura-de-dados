// # Projete uma struct para representar uma data
// # com dia, mês e ano. Em seguida:
// # a) Projete uma função que verifique se uma data é o último dia do ano.
// # b) Projete uma função que verifique se uma data é válida, considerando:
// #   - 0 < ano < 9999 e 0 < mês < 13
// #   - Meses 1, 3, 5, 7, 8, 10, 12 → 31 dias; meses 4, 6, 9, 11 → 30 dias;
// #     mês 2 → 28 dias
// # c) Projete uma função que receba duas datas e produza verdadeiro se a
// # primeira vem antes que a segunda.

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int dia;
    int mes;
    int ano;
} Data;

bool ehUltimoDiaDoAno(Data data) {
    if ( data.dia == 31 && data.mes == 12 )
        return true;
    
    return false;
}

bool dataEhValida(Data data) {
    const int ANO_MAXIMO = 9999;
    const int ANO_MINIMO = 1;
    const int MESES_COM_31_DIAS[] = { 1, 3, 5, 7, 8, 10, 12 };
    bool mesTem31Dias = false;

    if ( (data.ano < ANO_MINIMO || data.ano > ANO_MAXIMO) || (data.mes < 1 || data.mes > 12 ) )
        return false;
    
    if ( data.dia == 31 ) {
        for ( int i = 0; i < 7; i++ ) {
            if ( data.mes == MESES_COM_31_DIAS[i] )
                mesTem31Dias = true; 
        }

        if ( !mesTem31Dias ) return false;
    }
        
    if ( data.mes == 2 && data.dia > 28 )
        return false;
    
    return true;
}

bool vemAntes(Data dataInicial, Data dataFinal) {
    int somaDataInicial = dataInicial.ano * 10000 + dataInicial.mes * 100 + dataInicial.dia;
    int somaDataFinal = dataFinal.ano * 10000 + dataFinal.mes * 100 + dataFinal.dia;

    return somaDataInicial < somaDataFinal;
}

int main() {
    bool dataEhUltimoDiaDoAno;
    Data dataUltimoDia = { 31, 12, 2024 };

    dataEhUltimoDiaDoAno = ehUltimoDiaDoAno(dataUltimoDia);
    
    if (dataEhUltimoDiaDoAno == 1) 
        printf("%d/%d/%d é o último dia do ano\n", dataUltimoDia.dia, dataUltimoDia.mes, dataUltimoDia.ano);
    else
        printf("%d/%d/%d não é o último dia do ano\n", dataUltimoDia.dia, dataUltimoDia.mes, dataUltimoDia.ano);


    bool dataValida;
    Data data = { 1, 1, 2024 };

    dataValida = dataEhValida(data);

    if (dataValida == 1) 
        printf("%d/%d/%d é uma data válida\n", data.dia, data.mes, data.ano);
    else
        printf("%d/%d/%d não é uma data válida\n", data.dia, data.mes, data.ano);

    bool dataXVemAntesdeY;
    Data dataX = { 31, 10, 2023 };
    Data dataY = { 15, 12, 2023 };


    dataXVemAntesdeY = vemAntes(dataX, dataY);

    if (dataXVemAntesdeY == 1) 
        printf(
            "%d/%d/%d vem antes de %d/%d/%d\n", 
            dataX.dia, dataX.mes, dataX.ano,
            dataY.dia, dataY.mes, dataY.ano
        );
    else
        printf(
            "%d/%d/%d não vem antes de %d/%d/%d\n", 
            dataX.dia, dataX.mes, dataX.ano,
            dataY.dia, dataY.mes, dataY.ano
        );

    return 0;
}