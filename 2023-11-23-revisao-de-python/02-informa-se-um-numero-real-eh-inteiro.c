// # Projete uma função que informe se um determinado número real 
// # também é um inteiro. A seguir, faça uma função principal (main)
// # que peça para o usuário digitar um número e informe se ele é um
// # real ou um real inteiro.
#include <stdbool.h>
#include <stdio.h>

bool eh_inteiro(float n) {
    if ( n - (int)n == 0 ) {
        return true;
    }

    return false;
}

int main() {
    float n;
    bool ehInteiro; 

    n = 10.0;
    ehInteiro = eh_inteiro(n);
    if (ehInteiro) {
        printf("O número %.1f é inteiro\n", n);
    } else {
        printf("O número %.1f não é inteiro\n", n);
    }
    
    n = 1.2;
    ehInteiro = eh_inteiro(n);
    if (ehInteiro) {
        printf("O número %.1f é inteiro\n", n);
    } else {
        printf("O número %.1f não é inteiro\n", n);
    }

    return 0;
}