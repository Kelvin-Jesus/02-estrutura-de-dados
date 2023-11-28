#include <stdlib.h>
#include <stdio.h>

int* divisores(int n) {
    int* listaDeDivisores = NULL;

    int contador = 0;
    for ( int i = 1; i <= n; i++ ) {
        if ( n % i == 0 ) {
            listaDeDivisores = realloc(listaDeDivisores, (contador + 1) * sizeof(int));
            listaDeDivisores[contador] = i;
            contador++;
        }
    }

    return listaDeDivisores;
}

int main() {
    int* divisoresDeCinco;
    divisoresDeCinco = divisores(5); // [1, 5]
    for ( int i = 0; i < 2; i++ ) {
        printf("%d ", divisoresDeCinco[i]);
    }

    printf("\n");
    divisoresDeCinco = divisores(10); // [1, 2, 5, 10]
    for ( int i = 0; i < 4; i++ ) {
        printf("%d ", divisoresDeCinco[i]);
    }

    printf("\n");
    divisoresDeCinco = divisores(15); // [1, 3, 5, 15]
    for ( int i = 0; i < 4; i++ ) {
        printf("%d ", divisoresDeCinco[i]);
    }

    printf("\n");
    divisoresDeCinco = divisores(150); // [1, 2, 3, 5, 6, 10, 15, 25, 30, 50, 75, 150]
    for ( int i = 0; i < 12; i++ ) {
        printf("%d ", divisoresDeCinco[i]);
    }
    
}