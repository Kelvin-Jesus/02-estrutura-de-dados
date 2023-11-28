// # Projete uma função que receba três números inteiros 
// # e retorne o maior e o menor deles, nesta ordem.
#include <stdio.h>
#include <stdlib.h>

int* maior_e_menor(int n1, int n2, int n3) {
    int* arrayMaiorMenor = malloc(2 * sizeof(int));
    int maior = n1;
    int menor = n1;

    if (n2 > n1 && n2 > n3) {
        maior = n2;
    } 
    
    else if ( n3 > n1) {
        maior = n3;
    }

    if (n2 < n1 && n2 < n3) {
        menor = n2;
    }

    else if ( n3 < n1 ) {
        menor = n3;
    }

    arrayMaiorMenor[0] = maior;
    arrayMaiorMenor[1] = menor;

    return arrayMaiorMenor;
}

int main() {
    int *result = maior_e_menor(1, 2, 3);
    printf("Maior: %d\n", result[0]);
    printf("Menor: %d\n", result[1]);
    // >>> maior_e_menor(1, 2, 3)
    // (3, 1)
    // >>> maior_e_menor(5, 15, 10)
    // (15, 5)
    // print(f"O maior é: {tuplaDeMaiorMenor[0]}")
    // print(f"O menor é: {tuplaDeMaiorMenor[1]}")
    return 0;
}