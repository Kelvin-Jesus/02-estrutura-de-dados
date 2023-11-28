// # Projete uma função que retorne, para um dado número inteiro
// # n, uma lista contento todos os pares de números inteiros cujo o
// # produto resulta em n.

// # Por simplicidade, considere que o par (x, y) é diferente de (y, x)
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int primeiro;
    int segundo;
} Conjunto;

Conjunto* conjuntos(int n) {
    Conjunto* lista = malloc(n * sizeof(Conjunto));
    int size = 0;

    for ( int i = 1; i <= n; i++ ) {
        for ( int j = 1; j <= n; j++ ) {
            if ( i * j != n ) continue;

            lista[size].primeiro = i;
            lista[size].segundo = j;
            size++;
        }
    }

    return lista;
}

int main() {
    Conjunto* conjuntosDeN;
    conjuntosDeN = conjuntos(5); // [{primeiro: 1, segundo: 5}]
    printf("[{%d, %d}]\n", conjuntosDeN[0].primeiro, conjuntosDeN[0].segundo);

    printf("\n");
    conjuntosDeN = conjuntos(150); // [{1, 150}, {2, 75}, {50, 3}, {5, 30}, {25, 6}, {10, 15}]
    for ( int i = 0; i < 6; i++ ) {
        if ( i == 0 ) printf("[ ");
        printf("{%d, %d} ", conjuntosDeN[i].primeiro, conjuntosDeN[i].segundo);
        if ( i == 5 ) printf("]\n");
    }
    //     >>> pares(10)
    //     [{1, 10}, {2, 5}]
    //     >>> pares(15)
    //     [{1, 15}, {3, 5}]
    //     >>> pares(150)
    //     

    // n: int = int(input("Digite um número inteiro: "))
    // print(f"Os conjuntos de inteiros que resultam em {n} são: {conjuntos(n)}")
}
