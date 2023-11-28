// # Projete uma função que calcule o fatorial de um número. 
// # A seguir, faça uma função principal que peça para o usuário 
// # digitar um número inteiro n e informe o valor de n!.
#include <stdio.h>

int fatorial(int n) {
    if ( n == 0 )
        return 1;

    return fatorial(n - 1) * n;
}


int main() {
    printf("%d\n", fatorial(0)); // 1
    printf("%d\n", fatorial(1)); // 1
    printf("%d\n", fatorial(2)); // 2
    printf("%d\n", fatorial(3)); // 6
    printf("%d\n", fatorial(4)); // 24
    printf("%d\n", fatorial(5)); // 120
    return 0;
}